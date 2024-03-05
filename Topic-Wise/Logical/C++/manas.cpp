const int param = 0, order = 0;
bool compareTo( const pair<pair<string, string>, pair<int, int>+
        &a, const pair<pair<string, string>, pair<int, int>> &b ){
    bool res;
    string paramOrder = a.first.second;
    int param = paramOrder[0] - '0';
    int order = paramOrder[1] - '0';
    if( param == 0 ){
        res = ( a.first < b.first );
    }
    else if( param == 1 ){
        res = ( a.second.first < b.second.first );
    }
    else{
        res = ( a.second.second < b.second.second );
    }
    if( order == 0 ){
        return res;
    }
    else{
        return !res;
    }
}

vector fetchItemsToDisplay(int numOfItems,map<string,pair<int,int>> &items, int sortParameter, int sortOrder, int itemsPerPage,
                           int pageNumber){
    //...//

    vector<pair<pair<string, string>, pair<int, int>>> adj;
    int n = numOfItems;
    string paramOrder = to_string( sortParameter ) + to_string( sortOrder );
    for( auto &t : items ){
        adj.push_back( {{t.first, paramOrder }, {t.second.first, t.second.second}} );
    }
    sort( adj.begin(  ), adj.end(  ), compareTo );

    vector<string> res;
    int i = pageNumber * itemsPerPage;
    int j = min( n, i + itemsPerPage );
    for( ; i < j; i++ ){
        res.push_back( adj[i].first.first );
    }
    return res;
}