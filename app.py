
from flask import Flask,request,render_template
import pickle


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('studentdetails.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        stschool=request.form['stschool']
        age=request.form['age']
        gen=request.form['gen']
        atype=request.form['atype']
        fsize=request.form['fsize']
        pstat=request.form['pstat']
        medu=request.form['medu']
        fedu=request.form['fedu']
        mjob=request.form['mjob']
        fjob=request.form['fjob']
        reas=request.form['reas']
        guard=request.form['guard']
        travel=request.form['travel']
        stutime=request.form['stutime']
        fail=request.form['fail']
        ssup=request.form['ssup']
        fsup=request.form['fsup']
        excls=request.form['excls']
        exact=request.form['exact']
        nursery=request.form['nursery']
        higher=request.form['higher']
        internet=request.form['internet']
        famrel=request.form['famrel']
        freetime=request.form['freetime']
        goout=request.form['goout']
        hstatus=request.form['hstatus']
        absence=request.form['absence']
        if stschool=='MS':
            school=1
        else:
            school=0
        age=int(age)-12
        if gen=='F':
            gen=0
        else:
            gen=1
        if atype=='U':
            atype=1
        else:
            atype=0
        if fsize=='GT3':
            fsize=0
        else:
            fsize=1
        if pstat=='A':
            pstat=0
        else:
            pstat=1
        if mjob=='Teacher':
            mj=4
        elif mjob=='Health':
            mj=1
        elif mjob=='Services':
            mj=3
        elif mjob=='at_home':
            mj=0
        else:
            mj=2
        if fjob=='Teacher':
            fj=4
        elif fjob=='Health':
            fj=1
        elif fjob=='Services':
            fj=3
        elif fjob=='at_home':
            fj=0
        else:
            fj=2
        if reas=='home':
            reas=1
        elif reas=='reputation':
            reas=3
        elif reas=='course':
            reas=0
        else:
            reas=2
        if guard=='mother':
            guard=1
        elif guard=='father':
            guard=0
        else:
            guard=2
        if ssup=='yes':
            ssup=1
        else:
            ssup=0
        if fsup=='yes':
            fsup=1
        else:
            fsup=0
        if excls=='yes':
            excls=1
        else:
            excls=0
        if exact=='yes':
            exact=1
        else:
            exact=0
        if nursery=='yes':
            nursery=1
        else:
            nursery=0
        if higher=='yes':
            higher=1
        else:
            higher=0
        if internet=='yes':
            internet=1
        else:
            internet=0
        data=[[int(school),int(age),int(gen),int(atype),int(fsize),int(pstat),int(medu),int(fedu),int(mj),int(fj),int(reas),int(guard),int(travel),int(stutime),int(fail),int(ssup),int(fsup),int(excls),int(exact),int(nursery),int(higher),int(internet),int(famrel),int(freetime),int(goout),int(hstatus),int(absence)]]
        print(data)
        loader=pickle.load(open('model.pkl','rb'))
        pred=loader.predict(data)[0]
        print("MOdel is working")
        print(pred)
    return render_template('studentdetails.html',prediction=pred)
if __name__=='__main__':
    app.run(debug=True)
