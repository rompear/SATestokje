function fillSymbolTable() {
    var aa = "";
    for (var ba in symbols) {
        aa += "<td>" + symbols[ba] + "</td>";
    }
    $("table#symbols").find("tr:first").html(aa);
}
fillSymbolTable();
var tableRows = "";
for (var row = 0; row != numberOfSudokuRows; ++row) {
    tableRows += "<tr>";
    for (var column = 0; column != numberOfSudokuColumns; ++column) {
        tableRows += "<td>&nbsp;</td>";
    }
    tableRows += "</tr>";
}
$("table#board").html(tableRows);
sudokuCells = {};
loopSudokus(function(ca, da, ea, fa, ga, ha) {
    $("#board").find("tr").slice(ca, ca + ea).each(function(ia, ja) {
        $(ja).find("td").slice(da, da + fa).each(function(ka, la) {
            $(la).addClass("cell");
            if (ha != 0 && ka != 0 && ka % ha == 0) {
                $(la).addClass("left");
            }
            if (ha != 0 && ka != fa - 1 && ka % ha == 2) {
                $(la).addClass("right");
            }
            if (ga != 0 && ia != 0 && ia % ga == 0) {
                $(la).addClass("top");
            }
            if (ga != 0 && ia != ea - 1 && ia % ga == 2) {
                $(la).addClass("bottom");
            }
            sudokuCells["R" + (ca + ia) + "C" + (da + ka)] = true;
        });
    });
});
model.addObserver(function(ma, na, oa, pa) {
    var qa = $("#symbols").find("td").eq(oa).text();
    var ra = $("#board").find("tr").eq(ma).find("td").eq(na);
    ra.text(qa);
    if (pa) {
        ra.addClass("locked");
    } else {
        ra.removeClass("locked");
    }
    if (pa) {
        for (ma = 0; ma != numberOfSudokuRows; ++ma) {
            for (na = 0; na != numberOfSudokuColumns; ++na) {
                if (model.getValue(ma, na) && !model.getLock(ma, na)) {
                    model.setValue(ma, na, 0, false);
                }
            }
        }
    }
});

function clearSelection() {
    $("#board").find("td").removeClass("selected").addClass("default");
}
clearSelection();
$("#board").find("td").click(function() {
    var sa = $(this).parent().index();
    var ta = $(this).index();
    if (sudokuCells["R" + sa + "C" + ta]) {
        clearSelection();
        $(this).removeClass("default").addClass("selected");
    }
});
$("#symbols").find("td").click(function() {
    var ua = $(this);
    var va = getSelection();
    model.setValue(va.currentRow, va.currentColumn, ua.index(), ua.index() !== 0);
});
$("body").keypress(function(wa) {
    var xa = getSelection();
    var ya = xa.currentRow;
    var za = xa.currentColumn;
    var ch = String.fromCharCode(wa.which);
    for (var Aa = 0; Aa != symbols.length; ++Aa) {
        if (ch.toUpperCase() == symbols[Aa].toUpperCase()) {
            model.setValue(ya, za, Aa, Aa !== 0);
            break;
        }
    }
}).keydown(function(Ba) {
    var Ca = getSelection();
    var Da = Ca.currentRow;
    var Ea = Ca.currentColumn;
    clearSelection();
    var Fa = Da;
    var Ga = Ea;
    var Ha;
    if (Ba.which == 40) {
        Ha = function() {
            Fa = (Fa + 1) % numberOfSudokuRows;
        };
    } else if (Ba.which == 38) {
        Ha = function() {
            Fa = (Fa + (numberOfSudokuRows - 1)) % numberOfSudokuRows;
        };
    } else if (Ba.which == 39) {
        Ha = function() {
            Ga = (Ga + 1) % numberOfSudokuColumns;
        };
    } else if (Ba.which == 37) {
        Ha = function() {
            Ga = (Ga + (numberOfSudokuColumns - 1)) % numberOfSudokuColumns;
        };
    }
    if (Ha) {
        do {
            Ha()
        }
        while (sudokuCells["R" + Fa + "C" + Ga] == undefined);
    }
    $("#board").find("tr").eq(Fa).find("td").eq(Ga).removeClass("default").addClass("selected");
});

function getSelection() {
    var Ia = $("#board").find("td.selected");
    var Ja = $(Ia).parent().index();
    var Ka = $(Ia).index();
    return {
        currentRow: Ja,
        currentColumn: Ka
    };
}
$("button#clear").click(function() {
    for (var La = 0; La != numberOfSudokuColumns; ++La) {
        for (var Ma = 0; Ma != numberOfSudokuRows; ++Ma) {
            if (model.getValue(La, Ma)) {
                model.setValue(La, Ma, 0, false);
            }
        }
    }
});

function getLockedValues() {
    var Na = new Values();
    var Oa, col;
    for (Oa = 0; Oa != numberOfSudokuColumns; ++Oa) {
        for (col = 0; col != numberOfSudokuRows; ++col) {
            if (model.getLock(Oa, col)) {
                Na["R" + Oa + "C" + col] = model.getValue(Oa, col);
            }
        }
    }
    return Na;
}

function transForm(row, col) {
    A = 0
    loopSudokus(function(Ta, Ua, Va, Wa, Xa, Ya) {
        for (var Za = 0; Za != Va; ++Za) {
            for (var $a = 0; $a != Wa; ++$a) {
                var ab = Ta + Za;
                var bb = Ua + $a;
                if(row == ab && col == bb) {
                    return A = 1
                }
            }
        }
    })

    return A

}

function printSudoku(grid) {
    htmlString = '['
    for(var i = 0; i< numberOfSudokuColumns; i++) {
        htmlString += '['
        for(var j = 0; j<numberOfSudokuRows; j++) {
            htmlString += grid[i][j]
            if(j<numberOfSudokuRows - 1){
                htmlString += ',';
            }
        }
        if(i<numberOfSudokuColumns - 1){
            htmlString += '], <br/>';
        } else {
            htmlString += ']';
        }
    }
    htmlString += ']<br/>'
    return htmlString
}
$("button#reload").click(function() {
    // JavaScript Document
    /* Symbols that are used. The first symbol is the "empty" symbol. */
    var symbols=[" ","1","2","3","4","5","6","7","8","9"];

    /* Calls fun for every normal sudoku that is part of the total sudoku variant. */
    function loopSudokus( fun ) {
        // topRow, topColumn, Rows, Columns, SubGridRows, SubGridColumns
        fun( 0, 0, 9, 9, 3, 3 );
        fun( $("#n_order").val(), $("#n_order").val(), 9, 9, 3, 3 );
    }
    var numberOfSudokuRows = $("#sudoku_length").val();
    var numberOfSudokuColumns = $("#sudoku_length").val();

    var head= document.getElementsByTagName('head')[0];
    var script= document.createElement('script');
    script.type= 'text/javascript';
    script.src= 'SudokSolver_files/solver.js';
    head.appendChild(script);


    var script2= document.createElement('script');
    script2.type= 'text/javascript';
    script2.src= 'SudokSolver_files/overlap_2sudoku91.js';
    head.appendChild(script2);

});

$("button#solve").click(function() {
    var Pa = getLockedValues();
    var Qa = getConstraints();
    var Ra = getParameters();

    var rows = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
    var cols = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
    var numbers = [1,2,3,4,5,6,7,8,9];
    var clean_array = new Array(numberOfSudokuColumns-1);
    for (var i = 0; i < numberOfSudokuColumns; i++) {
      clean_array[i] = new Array(numberOfSudokuRows-1);
    }
    for(var n = 0; n < 2; n++) {
        var counter = 0
        var Sa = new UniqueSolutionObserver();
        var Nas = new Values();

        for(var i = 0; i<5; i++){
            var rows_selected = Math.floor((Math.random() * numberOfSudokuRows) + 1);
            var cols_selected = Math.floor((Math.random() * numberOfSudokuColumns) + 1);
            var cell_i = transForm(rows_selected, cols_selected);
            if(cell_i != 0) {
                Nas["R" + rows_selected + "C" + cols_selected] = numbers[Math.floor(Math.random()*numbers.length)]
                counter += 1
            }
        }

        if (counter == 0) {
            continue
        }

        for(var i = 0; i< numberOfSudokuColumns; i++) {
            for(var j = 0; j<numberOfSudokuRows; j++) {
                clean_array[i][j] = 'x';
            }
        }

        Pa = Nas

        solve(Ra, Qa, Pa, Sa);
        if (Sa.getNumberOfSolutionsFound() >= 1) {
            loopSudokus(function(Ta, Ua, Va, Wa, Xa, Ya) {
                for (var Za = 0; Za != Va; ++Za) {
                    for (var $a = 0; $a != Wa; ++$a) {
                        var ab = Ta + Za;
                        var bb = Ua + $a;
                        var cb = Sa.getSolution()["R" + ab + "C" + bb];

                        clean_array[ab][bb] = cb
                        if (!model.getLock(ab, bb)) {
                            model.setValue(ab, bb, cb, false);
                        }
                    }
                }
            });
            if (Sa.getNumberOfSolutionsFound() > 1) {
                $("#romeo").append(printSudoku(clean_array));
                $("#romeo").append('<br/>');
                // alert("More than one solution found. Check the values that you entered.");
            } else {
                alert("Exactly one solution found.");
                $("#romeo").append(printSudoku(clean_array));
                $("#romeo").append('<br/>');
            }
        } else {
            console.log("NOTHING FOUND")
        }
    }
});
$("button#about").click(function() {
    alert("Sudoku solver\n\nHosted on www.midoku.nl\n\n(C) 2014, Renze de Waal\ne-mail: info@midoku.nl");
});