
    // JavaScript Document
/* Symbols that are used. The first symbol is the "empty" symbol. */
var symbols=[" ","1","2","3","4","5","6","7","8","9"];

/* Calls fun for every normal sudoku that is part of the total sudoku variant. */
function loopSudokus( fun ) {
    // topRow, topColumn, Rows, Columns, SubGridRows, SubGridColumns
    fun( 0, 0, 9, 9, 3, 3 );
    fun( 8, 8, 9, 9, 3, 3 );
}
// 9 + fun(x) =
var numberOfSudokuRows = 17;
var numberOfSudokuColumns = 17; //(fun_1 + 9)
