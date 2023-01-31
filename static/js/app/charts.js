var element = document.getElementById('month-debits').dataset;
var invoices = document.getElementById('debitsChart').dataset;

var debits = '';
var data_debits = [];
var invoices_debits = {};

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

for (var i in invoices) {
   debits = invoices[i]
}

debits = debits.replace('{', '').replace('}', '');
debits = debits.split(',');

var invoice_amount = 0;

for (var i in debits) {
   kv = debits[i].split(':');
   key = kv[0].replace('\'', '').replace('\'', '').trim();
   value = kv[1].replace('\'', '').replace('\'', '');
   value = parseFloat(value);
   invoices_debits[key] = value;
   invoice_amount += value;
}

for (var i in invoices_debits) {
   x = (invoices_debits[i] * 100) / invoice_amount;
   invoices_debits[i] = x;
}

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
         data: [
            invoices_debits.Fatura,
            invoices_debits.Fixo,
            invoices_debits.Variavel
         ],
         backgroundColor: ['#2C7BE5', '#A6C5F7', '#D2DDEC']
      }]
   }
});