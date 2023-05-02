var mergeTwoLists = function (list1, list2) {
  //create dummy node
  let curr = new ListNode();
  let dummy = curr;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      curr.next = list1;
      list1 = list1.next;
    } else {
      curr.next = list2;
      list2 = list2.next;
    }
    curr = curr.next;
    console.log(JSON.stringify(dummy));
  }
  if (list1) {
    curr.next = list1;
  } else {
    curr.next = list2;
  }
  // console.log(JSON.stringify(dummy))
  return dummy.next;
};
