//or create a hashmap to keep track on the nodes until a repeated node is found

var hasCycle = function (head) {
  let f = head;
  let s = head;
  while (f && f.next) {
    s = s.next;
    f = f.next.next;
    if (f == s) return true;
  }
  return false;
};
