
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
