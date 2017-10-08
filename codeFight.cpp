#include <iostream>
#include <vector>

bool checkValid(int i,int j,int _maxI,int _maxJ){
    if((i>_maxI)||(i<0))
        return false;
    
    if((j>_maxJ)||(j<0))
        return false;
    
    return true;
}

std::vector<std::vector<int>> minesweeper(std::vector<std::vector<bool>> matrix) {
    std::vector<std::vector<int>> _rs;
    int _maxI = matrix.size();
    int _maxJ = matrix[0].size();
    
    for(size_t i=0;i<matrix.size();i++){
        
        std::vector<int> _rsRow;
        for(size_t j=0;j<matrix[i].size();j++){
            int _countWeeper=0;
            if(checkValid(i+1,j+1,_maxI,_maxJ)&&matrix[i+1][j+1]){
                _countWeeper++;
            }
            if(checkValid(i,j+1,_maxI,_maxJ)&&matrix[i][j+1]){
                _countWeeper++;
            }
            if(checkValid(i+1,j,_maxI,_maxJ)&&matrix[i+1][j]){
                _countWeeper++;
            }
            if(checkValid(i,j-1,_maxI,_maxJ)&&matrix[i][j-1]){
                _countWeeper++;
            }
            if(checkValid(i-1,j-1,_maxI,_maxJ)&&matrix[i-1][j-1]){
                _countWeeper++;
            }
            if(checkValid(i-1,j,_maxI,_maxJ)&&matrix[i-1][j]){
                _countWeeper++;
            }
            if(checkValid(i+1,j-1,_maxI,_maxJ)&&matrix[i+1][j-1]){
                _countWeeper++;
            }
            if(checkValid(i-1,j+1,_maxI,_maxJ)&&matrix[i-1][j]+1){
                _countWeeper++;
            }
            _rsRow.push_back(_countWeeper);
        }
        
        _rs.push_back(_rsRow);
        
    }
    
    return _rs;
}

void main()
{
    std::vector<std::vector<int>> rs = minesweeper(std::vector<bool>(true, false, false),std::vector<bool>(false, true, false),std::vector<bool>(false, false, false));
}