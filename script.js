d3.queue()
            .defer(d3.json, "https://d3js.org/world-50m.v1.json")
            .defer(d3.tsv, "carbon.txt")
            .await(function (error, file1, file2) {