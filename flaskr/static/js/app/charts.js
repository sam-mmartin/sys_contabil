function createDictAnnualSums() {
   var annual_sums = document.getElementById('anualSums').dataset;
   var sum_months = '';
   var arr_months = [];
   var sums = {};

   for (var i in annual_sums) {
      sum_months = annual_sums[i];
   }

   sum_months = sum_months.replace('{', '');
   sum_months = sum_months.split('}, ');

   sum_months.forEach(item => {
      var months = [];
      var i = item.split(': {');

      for (var x = 0; x < i.length; x++) {
         i[x] = i[x].replace(/\{/g, '').replace(/}/g, '');
      }

      var dict = i[1].split(', ');
      var sum_dict = {};

      dict.forEach(item => {
         var kv = item.split(': ');
         sum_dict[kv[0]] = parseFloat(kv[1]);
      });

      i[0] = i[0].replace('\'', '').replace('\'', '');
      sums[i[0]] = sum_dict;
   });

   var cred = [];
   var deb = [];

   Object.entries(sums).forEach(([key, value]) => {
      Object.entries(value).forEach(([k, v]) => {
         if (k == 2) {
            cred.push(v / 50);
         } else if (k == 1) {
            deb.push(v / 50);
         }
      });
   });

   new Chart('anualSums', {
      type: 'line',
      options: {
         scales: {
            yAxisOne: {
               display: "auto",
               grid: { color: "#283E59" },
               ticks: {
                  callback: function (e) {
                     return `R$ ${(e * 50)}`;
                  },
               },
            },
         },
      },
      data: {
         labels: Object.keys(sums),
         datasets: [
            {
               label: "Entradas",
               data: cred,
               yAxisID: "yAxisOne",
            },
            {
               label: "Saidas",
               data: deb,
               yAxisID: "yAxisOne",
               hidden: !0,
            },
         ],
      },
   });
}

function createChartMonthDebits() {
   var element = document.getElementById('month-debits').dataset;
   var debits = '';
   var values = [];
   var dates = [];
   var data_debits = [];

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
}

function createChartInvoiceDebits() {
   var invoices = document.getElementById('debitsChart').dataset;
   var dict = {};
   var amount = 0;
   var inv_deb = '';

   for (var i in invoices) {
      inv_deb = invoices[i]
   }

   inv_deb = inv_deb.replace('{', '').replace('}', '');
   inv_deb = inv_deb.split(', ');

   inv_deb.forEach(item => {
      var i = item.split(': ');
      i[0] = i[0].replace('\'', '').replace('\'', '');
      dict[i[0]] = parseFloat(i[1]);
   });

   Object.entries(dict).forEach(([key, value]) => {
      amount += value;
   });

   for (var i in dict) {
      x = (dict[i] * 100) / amount;
      dict[i] = x;
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
         labels: Object.keys(dict),
         datasets: [{
            data: Object.values(dict),
            backgroundColor: ['#2C7BE5', '#A6C5F7', '#D2DDEC']
         }]
      }
   });
}

createDictAnnualSums();
createChartMonthDebits();
createChartInvoiceDebits();