start =int(input('input stsrt : '))
end =int(input('input end : '))
s=0
if end < start:
    end,start=start,end
n=start
while n<= end:
    s=s+n
    n=n+1
print('s=', s)
