def fibonacci_of(n):
    if n in (0,1):
        return n
    
    return fibonacci_of(n-1) + fibonacci_of(n-2)

[fibonacci_of(n) for n in range (15)]

import plotly.express as px

fig=px.line(x=[1,2,3,4],y=[1,4,9,16])
fig.show()

