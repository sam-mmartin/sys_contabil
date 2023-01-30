var element = document.getElementById('month-debits').dataset;
var debits = '';
var data_debits = [];

for (var i in element) {
   debits = element[i];
}

debits = debits.replace('[', '').replace(']', '');
debits = debits.split(',');

debits.forEach(item => {
   data_debits.push(parseFloat(item));
})

new Chart('month-debits', {
   type: 'bar',
   options: {
      scales: {
         y: {
            ticks: {
               callback: function (value) {
                  return 'R$ ' + value / 1000 + 'k';
               }
            }
         }
      }
   },
   data: {
      labels: [
         'Jan',
         'Fev',
         'Mar',
         'Abr',
         'Mai',
         'Jun',
         'Jul',
         'Agt',
         'Set',
         'Out',
         'Nov',
         'Dez'
      ],
      datasets: [{
         label: 'Débitos',
         data: data_debits
      }]
   }
});

new Chart('debitsChart', {
   type: 'doughnut',
   options: {
      plugins: {
         tooltip: {
            callbacks: {
               afterLabel: function () {
                  return '%'
               }
            }
         }
      }
   },
   data: {
      labels: ['Faturas', 'Fixos', 'Variaveis'],
      datasets: [{
         data: [60, 25, 15],
         backgroundColor: ['#2C7BE5', '#A6C5F7', '#D2DDEC']
      }]
   }
});