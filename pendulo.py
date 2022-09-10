import math
op=2
g=9.81
while op!=1:
    imp=open('rueda.dat','w')
    t=float(0)
    print "largo de la cuerda"
    l=float(raw_input())

    print "angulo inicial"
    ang=raw_input()

    print "aumento de tiempo"
    aum=float(raw_input())

    print "cuanto tiempo?"
    lim=float(raw_input())
    wo=0.0
    theta=math.pi*float(ang)/180.0
    fi=g*math.cos(theta)/l
    pos=[l*math.cos(theta),-1.0*l*math.sin(theta),0.0]
    imp.write(str(pos[0])+'  '+str(pos[1])+'  '+str(pos[2])+'\n')
    print pos
    while t<=lim:
        t=t+aum
        theta_o=theta
        theta=theta_o+wo*aum+0.5*fi*aum**2
        wo=(theta-theta_o)/aum
        pos=[l*math.cos(theta),-1.0*l*math.sin(theta),0]
        imp.write(str(pos[0])+'  '+str(pos[1])+'  '+str(pos[2])+'\n')
        print pos
        #print ('theta:'+str(theta)+'   theta_o:'+str(theta_o)+'   wo:'+str(wo)+'    fi:'+str(fi))
        fi=g*math.cos(theta)/l
    imp.close()
    print "otra?"
    op=raw_input()
