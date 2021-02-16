class BSTNode {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  // BinarySearchTree methods
  /*
    method: insert
    time complexity: O(log(n))
  */
  insert(data) {
    let newNode = new BSTNode(data);

    if (this.root === null) {
      this.root = newNode;
    } else {
      this.insertHelper(this.root, newNode);
    }
  }

  /*
    method: remove
    time complexity: O(log(n))
  */
  remove(data) {}

  // Helper functions
  findMaxNode() {
    let pointer = this.root;
    while (pointer.right !== null) {
      pointer = pointer.right;
    }
    return pointer;
  }

  findMinNode() {
    let pointer = this.root;
    while (pointer.left !== null) {
      pointer = pointer.left;
    }
    return pointer;
  }

  insertHelper(node, newNode) {
    if (newNode.data < node.data) {
      if (node.left === null) {
        node.left = newNode;
      } else {
        this.insertHelper(node.left, newNode);
      }
    } else {
      if (node.right === null) {
        node.right = newNode;
      } else {
        this.insertHelper(node.right, newNode);
      }
    }
  }

  inorder() {}

  preorder() {}

  postorder() {}
}

module.exports = BinarySearchTree;
