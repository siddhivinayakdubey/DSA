//<sum, divisor>
pair<int, int> rec(Employee *curr, pair<float, Employee*> &best) {
    int sum = curr->val, divisor = 1;

    if (curr->child.size() == 0)
        return {curr->val, 1};
    for (auto c: curr->child) {
        auto tmp = rec(c, best);
        sum += tmp.first;
        divisor += tmp.second;
    }

    double mean = (double)sum / divisor;

    if (best.first < mean)
        best = {mean, curr};
    return {sum, divisor};
}

Employee *highestTenure(Employee *curr) {
    pair<float, Employee *> c = {0, curr};
    rec(curr, c);
    return c.second;
}