const mergeKLists = (lists) => {
  let main = null;
 
  for (let head of lists) { // k
    main = merge(main, head); // nk
  }

  return main;
};


function merge(head1, head2) {
  if (!head1) return head2;
  if (!head2) return head1;
  
  if (head1.val < head2.val) {
      let rest = head1.next;
      head1.next = merge(rest, head2);
      return head1;
  } else {
      let rest = head2.next;
      head2.next = merge(rest, head1);
      return head2;
  }
};