const { test, expect } = require('@jest/globals');
const BinarySearchTree = require('./BinarySearchTree');

test(`new BST root is null`, () => {
  let BST = new BinarySearchTree();

  expect(BST.root).toBe(null);
});

// Test helper functions
test(`Find max. Node of BST`, () => {
  let BST = new BinarySearchTree();
  BST.insert(10);
  BST.insert(5);
  BST.insert(15);
  BST.insert(3);
  BST.insert(7);
  BST.insert(13);
  BST.insert(20);
  BST.insert(6);
  BST.insert(9);
  BST.insert(8);

  const maxNode = BST.findMaxNode();

  expect(maxNode.data).toBe(20);
});

test(`Find min. Node of BST`, () => {
  let BST = new BinarySearchTree();
  BST.insert(10);
  BST.insert(5);
  BST.insert(15);
  BST.insert(3);
  BST.insert(7);
  BST.insert(13);
  BST.insert(20);
  BST.insert(6);
  BST.insert(9);
  BST.insert(8);

  const minNode = BST.findMinNode();

  expect(minNode.data).toBe(3);
});

test(`Inorder traversal`, () => {});

test(`Preorder traversal`, () => {});

test(`Postorder traversal`, () => {});

// Test functions
test(`Inserting into BST`, () => {
  let BST = new BinarySearchTree();
  BST.insert(3);
  BST.insert(5);
  BST.insert(1);
  BST.insert(7);

  expect(BST.root.data).toBe(3);
  expect(BST.root.right.data).toBe(5);
  expect(BST.root.left.data).toBe(1);
  expect(BST.root.right.right.data).toBe(7);
});

test(`Removing from BST`, () => {
  let BST = new BinarySearchTree();
  BST.insert(10);
  BST.insert(5);
  BST.insert(15);
  BST.insert(3);
  BST.insert(7);
  BST.insert(13);
  BST.insert(20);
  BST.insert(6);
  BST.insert(9);
  BST.insert(8);

  BST.remove(9);
  expect(BST.root.left.right.right.data).toBe(8);

  BST.remove(7);
  expect(BST.root.left.right.data).toBe(9);
  expect(BST.root.left.right.left.data).toBe(6);

  BST.remove(10);
  expect(BST.root.data).toBe(13);
  expect(BST.root.left.data).toBe(5);
  expect(BST.root.right.data).toBe(15);
  expect(BST.root.right.right.data).toBe(20);
});
