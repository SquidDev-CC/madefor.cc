from dns.domains import domains
from typing import NamedTuple, Any, Union, Callable
from pathlib import Path

# Translation dictionaries for table alignment
left_rule = {'<': ':', '^': ':', '>': '-'}
right_rule = {'<': '-', '^': ':', '>': ':'}


descriptions_path = "descriptions"


def evalute_field(record, field_spec):
    """
    Evalute a field of a record using the type of the field_spec as a guide.
    """
    if isinstance(field_spec, int):
        return str(record[field_spec])

    if isinstance(field_spec, str):
        return str(getattr(record, field_spec))

    return str(field_spec(record))


class Align:
    LEFT = '<'
    RIGHT = '>'
    CENTER = '^'


class Alignment(NamedTuple):
    header: Align = Align.CENTER
    cells: Align = Align.LEFT


Alignments = list[Alignment]
Headings = list[str]

Record = tuple[Any]
Records = list[Record]

Field = Union[int, str, Callable]
Fields = list[Field]


def table(
    records: Records,
    headings: Headings,
    fields: Fields = None,
    alignments: Alignments = None
) -> str:
    """
    Based on https://stackoverflow.com/questions/13394140/generate-markdown-tables#answer-15445930
    """

    if not fields:
        fields = list(range(len(records[0])))

    num_columns = len(fields)

    # Compute the table cell data
    columns = [[] for _ in range(num_columns)]
    for record in records:
        for i, field in enumerate(fields):
            columns[i].append(evalute_field(record, field))

    # Fill out any missing alignment characters.
    extended_align = alignments or []

    if len(extended_align) > num_columns:
        extended_align = extended_align[0:num_columns]
    elif len(extended_align) < num_columns:
        extended_align += [
            Alignment(Align.CENTER, Align.LEFT)
            for _ in range(num_columns - len(extended_align))
        ]

    heading_align, cell_align = [x for x in zip(*extended_align)]

    field_widths = [
        len(max(column, key=len)) if len(column) > 0 else 0
        for column in columns
    ]
    heading_widths = [max(len(head), 2) for head in headings]
    column_widths = [max(x) for x in zip(field_widths, heading_widths)]

    heading_alignment = [
        f'{{:{align}{width}}}' for align,
        width in zip(heading_align, column_widths)
    ]
    cell_alignment = [
        f'{{:{align}{width}}}' for align,
        width in zip(cell_align, column_widths)
    ]

    heading_template = f'| {" | ".join(heading_alignment)} |'
    row_template = f'| {" | ".join(cell_alignment)} |'

    formatted_cells = [
        f'{left_rule[align]}{"-" * (width - 2)}{right_rule[align]}'
        for align, width in zip(cell_align, column_widths)
    ]
    ruling = f"| {' | '.join(formatted_cells)} |"

    output = [
        heading_template.format(*headings).rstrip(),
        ruling.rstrip()
    ]

    for row in zip(*columns):
        output.append(row_template.format(*row).rstrip())

    return "\n".join(output)


def get_source_icon(source_url) -> str:
    if source_url is None:
        return ""

    if source_url.startswith("https://github.com"):
        return f" [:octicons-mark-github-16:]({source_url})"

    return f" [:simple-git:]({source_url})"


def has_description(name: str) -> bool:
    path = Path(descriptions_path) / f"{name}.md"
    if path.is_file():
        return True

    return False


def get_description(name: str) -> str:
    path = Path(descriptions_path) / f"{name}.md"
    if not path.is_file():
        return

    with path.open() as file:
        content = file.read()

    content = content.strip()
    if not content.replace('*', '').endswith(('.', '!', '?')):
        content += '.'

    return content


def get_domain_table() -> str:
    headings: Headings = [
        "Domain",
        "CNAME",
        "Source"
    ]

    records: Records = []

    for name, domain in domains.items():
        cname = domain["cname"]
        records.append((
            f"[{name}](https://{name}.madefor.cc)<span style=\"color: gray\">.madefor.cc</span>"
            + (f" **[&para;](#{name})**" if has_description(name) else " "),
            f"[{cname}](https://{cname})",
            get_source_icon(domain.get("source_url"))
        ))

    return table(records=records, headings=headings)


def get_domain_list() -> str:
    domain_list = []

    for name, domain in domains.items():
        if has_description(name):
            description = get_description(name)
            source_icon = get_source_icon(domain.get("source_url"))
            domain_list.append(
                f"## [{name}](https://{name}.madefor.cc){source_icon}\n\n{description}")

    return "\n\n".join(domain_list)


def main() -> None:
    print(
        "# Domains\n"
        "\n"
        "You're looking for cool CC projects ? "
        "Then you might want to check out "
        "[awesome-computercraft](https://github.com/tomodachi94/awesome-computercraft) "
        "or the creations channel on our "
        "[discord](https://github.com/SquidDev-CC/madefor.cc).\n"
        "\n"
        f"{get_domain_table()}\n"
        "\n"
        f"{get_domain_list()}"
    )


if __name__ == "__main__":
    main()
