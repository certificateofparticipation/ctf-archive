#include <iostream>
using namespace std;

#define ull unsigned long long int

ull calc(int rs, int cs, int re, int ce, ull arr[256][256], ull sss[256][256]){
    ull ans;
    if(rs == re and cs == ce){
        ans = arr[rs][cs];
    }else if (rs == 0 and cs == 0)
    {
        ans = sss[re][ce];
    }else if (rs == 0)
    {
        ans = sss[re][ce] - sss[re][cs-1];
    }else if (cs == 0)
    {
        ans = sss[re][ce] - sss[rs-1][ce];
    }else 
    {
        ans = sss[re][ce] - sss[re][cs-1] - sss[rs-1][ce] + sss[rs-1][cs-1];
    }
    return ans;
}

int main(){
    int N;
    cin >> N;
    ull arr[256][256] = {0};
    ull sss[256][256] = {0};
    for(int r = 0; r < N; r++){
        for(int c = 0; c < N; c++){
            cin >> arr[r][c];
        }        
    }

    for(int r = 0; r < N; r++){
        for(int c = 0; c < N; c++){
            ull x;
            if(r == 0 && c == 0){
                x = 0;
            }else if (r == 0)
            {
                x = sss[r][c-1];
            }else if (c == 0)
            {
                x = sss[r-1][c];
            }else{
                x = sss[r][c-1] + sss[r-1][c] - sss[r-1][c-1];
            }
            sss[r][c] = x + arr[r][c];
        }    
    }

    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int x,y,xe,ye;
        cin >> x >> y >> xe >> ye;
        cout << calc(x,y,xe,ye,arr,sss) << endl;
    }
}