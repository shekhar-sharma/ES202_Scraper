"""Script to download data from ES2O2 data for county subdivisions in Massachusetts."""

from urllib.request import urlopen


CITY = "000061"  # Zip code
NAME = "Cambridge"
VALUES = {}

for year in range(2010, 2021):
    url = f"https://lmi.dua.eol.mass.gov/lmi/EmploymentAndWages/EAWResult?A=05&GA={CITY}&Y={year}&P=00&O=00&I=6244~4&Iopt=2&Dopt=TEXT#"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    start_index = 0
    VALUES[year] = [year]

    for i in range(16):
        test_idx = html.find("<td class=\"lmi__results_data right\">", start_index)
        start_index = test_idx + len("<td class=\"lmi__results_data right\">")
        end_index = html.find("</td>", start_index)
        value = html[start_index: end_index]
        VALUES[year].append(value)
        start_index = end_index

# Print the values found.
for year, vals in VALUES.items():
    vals: list = [NAME, CITY] + [int(str(val).replace(",", "").replace("$", "")) for index, val in enumerate(vals)]
    print(str(vals)[1:-1])
