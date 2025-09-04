def build_car(width):
    first='.-----------'+'-'*width + '.\n'
    second='| ### ||  ###' +  '#'*width + '\\\n'
    third='| ### ||  ####' +  '#'*width +'\\.\n'
    fourth='D     ||  ' + ' '*width +'<>    |------+\n'
    fifth='|  ______      '+' '* width+'/______ |\n'
    sixth=' \/ /..\ \_____'+'_'*width+'/ /..\ \|\n'
    seventh='    \__/       '+' '*width+'  \__/'
    return first+second+third+fourth+fifth+sixth+seventh

print(build_car(5))