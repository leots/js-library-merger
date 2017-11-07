from subprocess import call


def main():
    output_file = "merged-libs.js"
    output_minified_file = "merged-libs.min.js"

    base_dir = "lib/dev"

    # noinspection SpellCheckingInspection
    files_to_merge = [
        "leaflet.js",
        "leaflet.contextmenu.min.js",
        "leaflet.markercluster.js",
        "ag-grid.min.js",
        "highstock/highstock.js",
        "highstock/highcharts-3d.js",
        "highstock/highcharts-more.js",
        "highmaps/modules/map.js",
        "highstock/modules/exporting.js",
        "highstock/modules/data.js",
        "highstock/modules/treemap.js",
        "highstock/modules/drilldown.js",
        "highstock/modules/sunburst.js",
        "underscore-min.js",
        "angular.min.js",
        "angular-ui-router.min.js",
        "ocLazyLoad.min.js",
        "ui-bootstrap-tpls-2.5.0.min.js",
        "rzslider.min.js",
        "angular-bootstrap-checkbox.js",
        "ng-text-truncate.min.js",
        "angular-cookies.min.js",
        "select.min.js",
        "md5.js",
        "jsurl.js",
        "jquery-2.2.4.min.js",
        "selectivity-full.min.js"
    ]

    # Merge the files
    with open(output_file, "w", encoding="UTF-8") as outfile:
        for fname in files_to_merge:
            with open(base_dir + "/" + fname, "r", encoding="UTF-8") as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write("\n\n")

    # Run UglifyJS2
    call("uglifyjs " + output_file + " --compress --output " +
         output_minified_file, shell=True)


if __name__ == "__main__":
    main()
