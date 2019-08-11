/*
Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.) */



class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        vector<int> copyCells = cells;

        copyCells[0] = copyCells[cells.size() - 1] = 0;

        for (int i = 0; i < N; i ++){
            for (int j = 1; j < cells.size() - 1; j++) {
            if (cells[j - 1] == cells[j + 1]){
                copyCells[j] = 1;
            } else {
                copyCells[j] = 0;

            }
        }
			cells = copyCells;
        }
        return cells;

}
};


class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        vector<int> copyCells = cells;

        copyCells[0] = copyCells[cells.size() - 1] = 0;

        for (int i = 0; i < N; i ++){
            copyCells[1] = ((cells[0] == 1 && cells[2] == 1) || (cells[0] == 0 && cells[2] == 0)) ? 1: 0;
            copyCells[2] = ((cells[1] == 1 && cells[3] == 1) || (cells[1] == 0 && cells[3] == 0)) ? 1: 0;
            copyCells[3] = ((cells[2] == 1 && cells[4] == 1) || (cells[2] == 0 && cells[4] == 0)) ? 1: 0;
            copyCells[4] = ((cells[3] == 1 && cells[5] == 1) || (cells[3] == 0 && cells[5] == 0)) ? 1: 0;
            copyCells[5] = ((cells[4] == 1 && cells[6] == 1) || (cells[4] == 0 && cells[6] == 0)) ? 1: 0;
            copyCells[6] = ((cells[5] == 1 && cells[7] == 1) || (cells[5] == 0 && cells[5] == 0)) ? 1: 0;
            cells = copyCells;
            }

        return cells;
    }
};


// class Solution {
// public:
//     vector<int> prisonAfterNDays(vector<int>& cells, int N) {
//         vector<int> copyCells = cells;
//
//         if (N > 14){
// 			N = N % 14;
// 		}
//
// 		if (N%14 == 0) {
// 			N = 14;
// 		}
//
//         for (int i = 1; i < N + 1; i ++){
//             if (cells[i - 1] == cells[i + 1]){
//                 copyCells[i] = 1;
//             } else {
//                 copyCells[i] = 0;
//             }
// 			      cells = copyCells;
//         }
//
//         return cells;
//     }
// };
