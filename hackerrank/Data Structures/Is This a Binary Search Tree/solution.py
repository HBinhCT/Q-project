""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):
    def check_node(cur, min_val, max_val):
        if not cur:
            return True
        if cur.data <= min_val or cur.data >= max_val:
            return False
        return check_node(cur.left, min_val, cur.data) and check_node(cur.right, cur.data, max_val)

    return check_node(root, -1, 10001)
