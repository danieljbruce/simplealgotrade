var SqliteTester = function() {
    this.currentDBFile = null;
}

SqliteTester.prototype.executeButtonPressed = function() {
    var inputCommands = this.getUserCommands();
    
}

SqliteTester.getUserCommands = function(){
    var arrayOfSQLInput = $('.CodeMirror-code').children();
    var commandsSQL = [];
    for (var i = 0; i < arrayOfSQLInput.length; i++){
        commandsSQL.push($(arrayOfSQLInput[i]).find('pre span').text());
    }
    return commandsSQL;
}

    var oReq = new XMLHttpRequest(); /* yes, XHR */
    oReq.open("GET", '/' + file, true);
    oReq.responseType = "arraybuffer";
    oReq.onload = function(e) {
        /* For some unknown reason, Chrome slows to a crawl with typed arrays */
        var arraybuffer = oReq.response;
        var data = new Uint8Array(arraybuffer);
        var arr = new Array();
        for(var i = 0; i != data.length; ++i) arr[i] = data[i];

        DS(arr); /* Drop it like it's hot */
    }