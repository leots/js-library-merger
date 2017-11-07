from subprocess import call


def main():
    output_file = "merged-css.css"
    output_minified_file = "merged-css.min.css"

    base_dir = "css/dev"

    # noinspection SpellCheckingInspection
    files_to_merge = [
        "leaflet.css",
        "leaflet.contextmenu.min.css",
        "ag-grid.min.css",
        "theme-fresh.min.css",
        "bootstrap.min.css",
        "animate.css",
        "rzslider.min.css"
    ]

    # Merge the files
    with open(output_file, "w", encoding="UTF-8") as outfile:
        for fname in files_to_merge:
            with open(base_dir + "/" + fname, "r", encoding="UTF-8") as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write("\n\n")

    # Run UglifyCSS
    call("uglifycss " + output_file + " --ugly-comments --output " +
         output_minified_file, shell=True)


if __name__ == "__main__":
    main()
