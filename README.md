# branch_find
Simple module for finding necessary branch in json.
Returns a list of all paths to provided key/item converted to string which can than be evaluated.
Usage example see inside locate_branch.py.

Result examples:  
```
# locate()
['key1'][2]['races'][1]['begin_ts']['1']['cars'][3]['begin_ts']
[2]['races'][1]['begin_ts']['1']['cars'][3]['begin_ts']

# locate_with_dots()
# For mappings which support dot notations, see examples inside locate_branch.py:
.key1[2].races[1].begin_ts['1'].cars[3].begin_ts
[2].races[1].begin_ts['1'].cars[3].begin_ts

```
