var g_DB = new SQL.Database();

var g_readCommandsButton  = function() {
    
    $('.sqljs-console .output').text(JSON.stringify(g_getSelectStatementAsJSON($('.sqljs-console .text-read-commands').val())));
}

var g_writeCommandsButton = function() {
    g_DB.run($('.sqljs-console .text-write-commands').val());    
}

// Add listeners
$(document).ready(function(){
    $('.sqljs-console .button-write-commands').click(function(){g_writeCommandsButton();});
    $('.sqljs-console .button-read-commands').click(function(){g_readCommandsButton();});
    $('.time-series-render-button').click(function(){ g_SendJSONToPlot();});
});

function handleFileSelect(evt) {
    var files = evt.target.files; // FileList object

    // files is a FileList of File objects. List some properties.
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
        output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
        f.size, ' bytes, last modified: ',
        f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a', '</li>');
    }
    document.getElementById('list-file-output').innerHTML = '<ul>' + output.join('') + '</ul>';
}

g_getSelectStatementAsJSON = function(parameterSelectStatement){
    var output = [];
    var max_lines = 100;
    var line_count = 0;
    var stmt = g_DB.prepare(parameterSelectStatement);
    while (stmt.step() && (line_count < max_lines)) {
        // stmt.step();
        output.push(stmt.getAsObject());
        line_count = line_count + 1;
    }
    return output;
}

g_PopulateTimeSeriesSelector = function(){
    var jsonTimeSeriesSelections = g_getSelectStatementAsJSON('SELECT DISTINCT Entity FROM TimeSeriesData;');
    // jsonTimeSeriesSelections should be an array.
    if (typeof(jsonTimeSeriesSelections.length) !== 'undefined'){
        for (var i = 0; i < jsonTimeSeriesSelections.length; i++){
            if (typeof(jsonTimeSeriesSelections[i].Entity) !== 'undefined'){
                var entityjsonTimeSeriesSelection = jsonTimeSeriesSelections[i].Entity;
                $('.time-series-selector').append('<input type="checkbox" name="time-series" value="'+entityjsonTimeSeriesSelection+'">'+entityjsonTimeSeriesSelection + '<br>');
            }
        }
    }
}

g_RenderChart = function(){
    
}

g_UpdateJSONForChart = function(){
    
}

g_SendJSONToPlot = function(){
    // Get series names.
    var plotData = {};
    var arrSeries = []
    var checkBoxes = $('.time-series-selector input:checked');
    for (var i = 0; i < checkBoxes.length; i++){
        arrSeries.push(checkBoxes[i].value);
    }
    var strSeriesListSQL = JSON.stringify(arrSeries);
    strSeriesListSQL = strSeriesListSQL.slice(1, strSeriesListSQL.length-1);
    strSeriesListSQL = '(' + strSeriesListSQL + ')';
    var jsonTimeSeriesData = g_getSelectStatementAsJSON('SELECT * FROM TimeSeriesData WHERE Entity IN '+strSeriesListSQL + ' ORDER BY Entity, Time');
    if (typeof(jsonTimeSeriesData.length) !== 'undefined'){
        for (var i = 0; i < jsonTimeSeriesData.length; i++){
            var entity = plotData[jsonTimeSeriesData[i].Entity];
            if (typeof(plotData[entity]) === 'undefined'){
                plotData[entity] = {};
                plotData[entity].name = entity;
                plotData[entity].mode = 'lines';
                plotData[entity].x = [];
                plotData[entity].y = [];
            }
            plotData[entity].x.push(jsonTimeSeriesData[i].Time);
            plotData[entity].y.push(jsonTimeSeriesData[i].Value);
        }
    }
    // Convert JSON and render plot.
    var finalPlotData = [];
    for (var key in plotData) {
        if (plotData.hasOwnProperty(key)) {
            finalPlotData.push(plotData[key]);
        }
    }
    var layout = {
        title:'TimeSeriesData'
    };
    Plotly.newPlot('graph', finalPlotData, layout);
}


var xhr = new XMLHttpRequest();
//xhr.open('GET', '/shared-with-backend/simplealgotrade.db', true);
// xhr.open('GET', '/database/timeseriesdata.csv', true);
xhr.open('GET', '/database/justatest.db', true);
xhr.responseType = 'arraybuffer';
xhr.onload = function(e) {
    // new SQL.Database(new Uint8Array(this.response)); // Try this in the console.
    var arrayBuffer = xhr.response;
    var data = new Uint8Array(arrayBuffer);
    g_DB = new SQL.Database(data);
    // g_DB.exec("SELECT * FROM SQLITE_MASTER"); // This should give us a list tables in the database // Try this in the console.
    // g_DB.prepare("SELECT * FROM TimeSeriesData"); // Try this in the console.
    g_PopulateTimeSeriesSelector();
    $('.time-series-selector input').click(function(){g_UpdateJSONForChart();});
    //var contents = db.exec("SELECT * FROM my_table");
    // contents is now [{columns:['col1','col2',...], values:[[first row], [second row], ...]}]
    var elements = $('.')
};
xhr.onerror = function(e){
    console.log("Could not load the SQLite database.");
};
xhr.send();

