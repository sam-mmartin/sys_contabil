window.onload = function () {

   document.querySelectorAll('.delete_register').forEach((link) => {
      link.addEventListener('click', (event) => {
         var el_node = link.closest('tr').childNodes[1].innerHTML;
         console.log(el_node);
         el_node = el_node.trim();
         var input = document.getElementById('delete_id');
         input.value = el_node;
      });
   });
}