import c4d
from c4d.modules import mograph as mo

def main():
    # Get MoData
    md = mo.GeGetMoData(op)
    if md is None:
        return

    # Get the count of clones
    cnt = md.GetCount()
    if cnt == 0:
        return

    # Get clone matrices and colors
    marr = md.GetArray(c4d.MODATA_MATRIX)
    carr = md.GetArray(c4d.MODATA_COLOR)

    # Reverse the matrices and colors
    marr.reverse()
    carr.reverse()

    # Set the reversed arrays back to MoData
    md.SetArray(c4d.MODATA_MATRIX, marr, True)
    md.SetArray(c4d.MODATA_COLOR, carr, True)

