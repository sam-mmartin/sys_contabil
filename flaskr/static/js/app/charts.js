var element = document.getElementById('month-debits').dataset;
var invoices = document.getElementById('debitsChart').dataset;
var annual_credits = document.getElementById('anualCredits').dataset;

var debits = '';
var inv_deb = ''
var data_debits = [];
var values = [];
var dates = [];
var invoice_amount = 0;

for (var i in element) {
   debits = element[i];
}

debits = debits.replace(/\{/g, '').replace(/}/g, '');
debits = debits.split(',');

debits.forEach(item => {
   temp = item.split(':');
   dates.push(temp[0]);
   values.push(parseFloat(temp[1]));
});

values.forEach(item => {
   data_debits.push(item / 50);
});

for (var i in invoices) {
   inv_deb = invoices[i]
}

inv_deb = inv_deb.replace('{', '').replace('}', '');
inv_deb = inv_deb.split(',');

var invoices_debits = createDict(inv_deb);
Object.entries(invoices_debits).forEach(([key, value]) => {
   invoice_amount += value;
});

for (var i in invoices_debits) {
   x = (invoices_debits[i] * 100) / invoice_amount;
   invoices_debits[i] = x;
}

var credits = '';

for (var i in annual_credits) {
   credits = annual_credits[i];
}

credits = credits.replace('{', '').replace('}', '');
credits = credits.split(',');
var credits_dict = createDict(credits);

function createDict(obj) {
   dict = {};

   for (var i in obj) {
      kv = obj[i].split(':');
      key = kv[0].replace('\'', '').replace('\'', '').trim();
      value = kv[1].replace('\'', '').replace('\'', '');
      value = parseFloat(value);
      dict[key] = value;
   }

   return dict;
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
      labels: Object.keys(invoices_debits),
      datasets: [{
         data: Object.values(invoices_debits),
         backgroundColor: ['#2C7BE5', '#A6C5F7', '#D2DDEC']
      }]
   }
});

new Chart('anualCredits', {
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
      labels: Object.keys(credits_dict),
      datasets: [
         {
            label: "Entradas",
            data: Object.values(credits_dict),
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
