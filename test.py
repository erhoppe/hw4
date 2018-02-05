
#to enumerate over the list in reverse
for i, e in reversed(list(enumerate(a))):
...     print i, e


#code from C++
for (auto& node : node_vect) {
		vector<int> coords = node.coordinates;
		a = coords[0];
		int a_plus = a<a_size; //will be evaluated to one plus the original int if that won't exceed the size of sequence
		for (int a_i = a; a_i <= a + a_plus; a_i++) {
			b = coords[1];
			int b_plus = b<b_size;
			for (int b_i = b; b_i <= b + b_plus; b_i++) {
				c = coords[2];
				int c_plus = c<c_size;
				for (int c_i = c; c_i <= c + c_plus; c_i++) {
					//cout << a_i << "," << b_i << "," << c_i << endl;
					inner_vect = {a_i, b_i, c_i};
					//we now have both the parent and child nodes
					//need to make the edge between
					//use the node_map to get the pointer to each and store in to_node and from_node
					//get the string of aas/gaps from the coordinates
					// - +1 in a direction means that the sequence has an amino acid in that direction; else a gap
					// - will need to work out the indexing on the small set

				}
			}
		}
	}


# for row in new_nodes:
# print(row) #access values with row[0], etc.
# print(node_max_arr(tuple(row)))


#### IMPORTANT ACCESS OF ARRAYS ######
# for x in np.nditer(a, op_flags=['readwrite']):
#    x[...] = 2 * x
# if you don't do this, it won't change the value

### IMPORTANT Multi Index: https://docs.scipy.org/doc/numpy/reference/arrays.nditer.html



# for i in range(new_nodes.size-1):
# if np.less_equal(new_nodes[i,:],len_arr):
#   print(new_nodes[i])


# access item with  new_nodes.item

## for node in node_arr
#### generate children nodes
#### generate score based on the vector indices
#### if that score is bigger than the current score, replace and save indices to max parent dict
###can maybe use where conditional to grab the original set of children node values and replace if better

dict = {(0, 1, 1): (0, 0, 1)}
print(dict)

# while (a_i <= len_a + 1 or b_i <= len_b + 1 or c_i <= len_c + 1):
#    print (a_i, b_i, c_i)
#    a_i += 1
#    b_i += 1
#    c_i += 1

# we should use array addition, I think to generate the possible nodes from each parent