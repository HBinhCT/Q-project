d = int(input())
oc, of, od = map(int, input().strip().split())
cs, cb, cm, cd = map(int, input().strip().split())
o = oc + (d - of) * od
c = cb + d / cs * cm + d * cd
print("Online Taxi" if o <= c else "Classic Taxi")
