var element = document.getElementById('month-debits').dataset;
var invoices = document.getElementById('debitsChart').dataset;

var debits = '';
var data_debits = [];
var invoices_debits = {};

for (var i in element) {
   debits = element[i];
}

console.log(debits);

debits = debits.replace(/\{/g, '').replace(/}/g, '');
debits = debits.split(',');

values = [];
dates = [];

debits.forEach(item => {
   temp = item.split(':');
   dates.push(temp[0]);
   values.push(parseFloat(temp[1]));
});

console.log(dates);
console.log(values);

values.forEach(item => {
   data_debits.push(item / 50);
});

console.log(data_debits);

inv_deb = ''

for (var i in invoices) {
   inv_deb = invoices[i]
}

console.log(inv_deb)

inv_deb = inv_deb.replace('{', '').replace('}', '');
inv_deb = inv_deb.split(',');

var invoice_amount = 0;

for (var i in inv_deb) {
   kv = inv_deb[i].split(':');
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

new Chart('month-debits', {
   type: 'bar',
   options: {
      scales: {
         y: {
            ticks: {
               callback: function (value) {
                  return 'R$ ' + value * 50;
               }
            }
         }
      }
   },
   data: {
      labels: dates,
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
         data: [
            invoices_debits.Fatura,
            invoices_debits.Fixo,
            invoices_debits.Variavel
         ],
         backgroundColor: ['#2C7BE5', '#A6C5F7', '#D2DDEC']
      }]
   }
});

new Chart('anualDebits', {
   type: 'line',
   options: {
      scales: {
         yAxisOne: {
            display: "auto",
            grid: { color: "#283E59" },
            ticks: {
               callback: function (e) {
                  return e + "k";
               },
            },
         },
         yAxisTwo: {
            display: "auto",
            grid: { color: "#283E59" },
            ticks: {
               callback: function (e) {
                  return e + "%";
               },
            },
         },
      },
   },
   data: {
      labels: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec",
      ],
      datasets: [
         {
            label: "Entradas",
            data: [5321.74, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            yAxisID: "yAxisOne",
         },
         {
            label: "Saidas",
            data: [5712.12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            yAxisID: "yAxisOne",
            hidden: !0,
         },
         {
            label: "Balanço",
            data: [40, 57, 25, 50, 57, 32, 46, 28, 59, 34, 52, 48],
            yAxisID: "yAxisTwo",
            hidden: !0,
         },
      ],
   },
});
