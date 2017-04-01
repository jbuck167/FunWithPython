## Iterate through instructions
## Make a comment for all "cmp" instrructions
## Partially from http://www.openrce.org/articles/full_view/11

from sets import Set

ea = ScreenEA()

callers = dict()
callees = dict()
mnemonics = dict()
FunctionDict = dict()

def ParseFunction():
    for seg in Segments():
        for head in range(seg, SegEnd(seg)):
            if isCode(GetFlags(head)):
                mnem = GetMnem(head)
                if mnem == 'call':
                    Name = GetFunctionName(head)
                    Opnd = GetOpnd(head, 0)
                    if (Opnd.find("strcpy") > -1 or Opnd.find("sprintf")  > -1 or Opnd.find("strncpy")  > -1 or Opnd.find("wcsncpy") > -1  or Opnd.find("swprintf") > -1 ):
                        print Name, ':', hex(head), ':', Opnd



def ParseFunctions(fun):
    if fun in FunctionDict.keys():
        return
    f_name = GetFunctionName(fun)
    callers[f_name] = Set(map(GetFunctionName, CodeRefsTo(fun, 0)))
    for ref in CodeRefsTo(fun, 0):
        caller_name = GetFunctionName(ref)
        callees[caller_name] = callees.get(caller_name, Set())
        callees[caller_name].add(f_name)
    mnem = GetMnem(fun)
    FunctionDict[fun] = 1
    mnemonics[mnem] = mnemonics.get(mnem, 0)+1
    MakeComm(fun, "call instruction")
    SetColor(fun, CIC_ITEM, 0xF0F02F)
    return


# For each of the segments
#for fun in Functions(SegStart(ea), SegEnd(ea)):
#    ParseFunctions(fun)
#for seg in Segments():
#    for head in Heads(seg, SegEnd(seg)):
#        ParseFunctions(head)

ParseFunction()

# Get the list of all functions
#functions = Set(callees.keys()+callers.keys())

# For each of the functions, print the number of functions calling it and
# number of functions being called. In short, indegree and outdegree
#for f in functions:
#print 'function[ %s ]:called[%d]:calls[%d]' % (f, len(callers.get(f, [])), len(callees.get(f, [])))

# Sort the mnemonics by number of occurrences
#sorted = map(lambda x:(x[1], x[0]), mnemonics.items())
#sorted.sort()

# Print the sorted list
#for mnemonic, count in sorted:
#print mnemonic, count
