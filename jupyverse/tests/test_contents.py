import os
from pathlib import Path

from utils import create_content, clear_content_values, sort_content_by_name


def test_tree(client, tmp_path):
    os.chdir(tmp_path)
    dname = Path(".")
    expected = []
    # write some files with different size
    for size in range(7, 13):
        fname = f"file_size_{size}"
        with (dname / fname).open("w") as f:
            f.write("-" * size)
        expected.append(
            create_content(
                content=None,
                type="file",
                size=size,
                mimetype="text/plain",
                name=fname,
                path=str(dname / fname),
                format=None,
            )
        )
    # write some directories
    for i in range(3):
        sub_dname = f"directory_{i}"
        (dname / sub_dname).mkdir()
        expected.append(
            create_content(
                content=None,
                type="directory",
                size=None,
                mimetype=None,
                name=sub_dname,
                path=str(dname / sub_dname),
                format="json",
            )
        )
    expected = create_content(
        content=expected,
        type="directory",
        size=None,
        mimetype=None,
        name="",
        path=str(dname),
        format="json",
    )
    response = client.get("/api/contents?content=1")
    actual = response.json()
    # ignore modification and creation times
    clear_content_values(actual, keys=["created", "last_modified"])
    # ensure content names are ordered the same way
    sort_content_by_name(actual)
    sort_content_by_name(expected)
    assert actual == expected
