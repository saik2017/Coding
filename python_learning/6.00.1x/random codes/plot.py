import pylab as plt

def retire(monthly,rate,terms):
    savings=[0]
    base=[0]
    monthly_rate=rate/12.0
    for i in range(terms):
        base+=[i]
        savings+=[savings[-1]*(1+monthly_rate)+monthly]
    return base,savings

def displayRetireWMonthlies(monthlies,rate,terms):
    plt.figure("Retire month")
    plt.clf()
    for monthly in monthlies:
        xvals,yvals=retire(monthly,rate,terms)
        plt.plot(xvals,yvals,label='retire'+str(monthly))
        plt.legend(loc='upper left')
    plt.show(block=False)
l=[500,600,700,800,900,1000,1100]
#displayRetireWMonthlies(l,0.05,40*12)

def displayRetireWRates(monthly,rates,terms):
    plt.figure("Retire rate")
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label=' retire ' +str(monthly)+ str(rate*100)+'%')
        plt.legend(loc='upper left')
    plt.show()
#displayRetireWRates(800,[0.03,0.05,0.07],40*12)

def displayRetireWmonthsAndRates(monthlies,rates,terms):
    plt.figure("Retire both")
    plt.clf()
    plt.xlim(terms-119,terms)
    monthLabels=['r','b','g','k']
    rateLabels=['-','o','--']
    for i in range(len(monthlies)):
        monthly=monthlies[i]
        monthLabel=monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate=rates[j]
            rateLabel=rateLabels[j%len(rateLabels)]
            xvals,yvals=retire(monthly,rate,terms)
            plt.plot(xvals,yvals,monthLabel+rateLabel,label='retire: '+str(monthly)+': '+str(int(rate*100))+'%')
            plt.legend(loc='upper left')
    plt.plot()
    plt.show()

displayRetireWmonthsAndRates([500,700,900,1100],[0.03,0.05,0.07],40*12)
