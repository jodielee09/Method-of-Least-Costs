# Method-of-Least-Costs
Calculating an optimal solution of transportation problems

The Method of Least Costs, also known as The Matrix Minimisation Method,uses the values of the transport costs to create an initial solution.  This is more efficient than the North-West Corner Method as it takes into consideration the costs as well as the supply and demand, whereas the North-West Corner Method only considers supply and demand for the upper left most squares. 

Step 1:  Locate the lowest shipping cost(s) in the grid. If there is more than one, select the route that can hold the most units.\
Step 2:  Put as much as possible into the selected route, and cross out the corre-sponding supply or demand row that has been fulfilled.\
Step 3:  Repeat steps 1-2 until all supply and demand needs have been met.
