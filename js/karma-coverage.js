const percentage = {
    lines: 60,
    statements: 60,
    functions: 60,
    branches: 50
}
var summary = require('./karma/coverage/coverage-summary.json');

for (let res in summary.total) {
    if (summary.total[res].pct < percentage[res]) {
        throw new Error(
            `Coverage too low on ${res},
            expected: ${percentage[res]},
            got: ${summary.total[res].pct}`
        );
    }
}