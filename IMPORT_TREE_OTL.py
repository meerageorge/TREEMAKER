#!/usr/bin/python
# -*- coding: utf-8 -*-
# import modules
#CREATING ALL THE TREE NODES
import toolutils
import soptoolutils
import sys
from PySide import QtGui, QtCore
import hou

sel_node = hou.selectedNodes()
if len(sel_node) < 1:
    hou.ui.displayMessage('select a ground')
else:

    # create node

    hou.hda.installFile('/SCORPION/PYTHON/TREE_PAINTING/final_code/SideFX__deciduoustree.otl'
                        )
    x = hou.node('/obj/deciduoustree1/treesys1/OUT')
    sel_node = hou.selectedNodes()
    sel_node_path = sel_node[0].path()
    print sel_node_path
    obj_ctxt = hou.node('obj')
    obj = hou.node('obj')
    geo = obj.createNode('geo', run_init_scripts=False)
    grnd = geo.createNode('object_merge', 'GROUND')
    uvtxtr = geo.createNode('texture')
    vopsopptcd = geo.createNode('vopsop', run_init_scripts=False)
    pnt = geo.createNode('paint')
    dlt_colordarea = geo.createNode('delete')
    switchwithexp = geo.createNode('switch')
    switchwoexp = geo.createNode('switch')
    assmbl = geo.createNode('assemble')
    add = geo.createNode('add')
    attbtrnfr = geo.createNode('attribtransfer')
    attrbwrngl = geo.createNode('attribwrangle')
    pscale_wrngl = geo.createNode('attribwrangle',
                                  'attribwrangle_pscale')
    orint_wrngl = geo.createNode('attribwrangle',
                                 'attribwrangle_rotation')
    objmrg = geo.createNode('object_merge')
    trns = geo.createNode('xform')
    cpy = geo.createNode('copy')
    unpck = geo.createNode('unpack')
    attrbwrngl_aftunpck = geo.createNode('attribwrangle')
    null = geo.createNode('null')
    mrg = geo.createNode('merge')

    # set input

    pnt.setInput(0, grnd)
    uvtxtr.setInput(0, grnd)
    vopsopptcd.setInput(0, uvtxtr)
    switchwoexp.setInput(0, vopsopptcd)
    switchwoexp.setInput(1, pnt)
    switchwithexp.setInput(0, vopsopptcd)
    switchwithexp.setInput(1, pnt)
    dlt_colordarea.setInput(0, switchwoexp)
    assmbl.setInput(0, dlt_colordarea)
    add.setInput(0, assmbl)
    attbtrnfr.setInput(0, add)
    attbtrnfr.setInput(1, dlt_colordarea)
    attrbwrngl.setInput(0, attbtrnfr)
    pscale_wrngl.setInput(0, attrbwrngl)
    orint_wrngl.setInput(0, pscale_wrngl)
    trns.setInput(0, objmrg)
    cpy.setInput(0, trns)
    cpy.setInput(1, orint_wrngl)
    unpck.setInput(0, cpy)
    attrbwrngl_aftunpck.setInput(0, unpck)
    null.setInput(0, attrbwrngl_aftunpck)
    geo.layoutChildren()
    mrg.setInput(0, null)
    mrg.setInput(1, switchwithexp)

    # set parm

    grnd_path = grnd.parm('objpath1')
    grnd_path.set(sel_node_path)
    uvtxtr_coord = uvtxtr.parm('coord')
    uvtxtr_coord.set(0)
    hou.parmTuple('/obj/geo2/paint1/bg')
    pnt_bg = pnt.parmTuple('bg')
    pnt_bg[0].set(0)
    pnt_bg[1].set(0)
    pnt_bg[2].set(0)
    hou.parm('/obj/geo2/switch2/input')
    switchwoexp_input = switchwoexp.parm('input')
    switchwoexp_input.set(1)
    pntfg = pnt.parmTuple('fg')
    pntfg[0].set(0)
    pntfg[1].set(0)
    pntfg[2].set(0)
    pnt.parm('flood').pressButton()
    pntfg[0].set(1)
    pntfg[1].set(0)
    pntfg[2].set(0)
    dltop = dlt_colordarea.parm('negate')
    dltop.set(1)
    dltenty = dlt_colordarea.parm('entity')
    dltenty.set(1)
    dltgpop = dlt_colordarea.parm('groupop')
    dltgpop.set(2)
    dltfltr = dlt_colordarea.parm('filter')
    dltfltr.setExpression('$CR>.1 || $CG>.1|| $CB>.1')
    switchwithexp_input = switchwithexp.parm('input')
    switchwithexp_input.setExpression('ch("../switch2/input")')
    assmbl_pckgeo = assmbl.parm('pack_geo')
    assmbl_pckgeo.set(1)
    add_dltgeokppts = add.parm('keep')
    add_dltgeokppts.set(1)
    attbttrnf_thdist = attbtrnfr.parm('thresholddist')
    attbttrnf_thdist.set(1)
    attrbtwrnglsnpt = attrbwrngl.parm('snippet')
    attrbtwrnglsnpt.set('v@x=@Cd;')
    cpydoattr = cpy.parm('doattr')
    cpydoattr.set(1)
    cpypckbfrcpy = cpy.parm('pack')
    cpypckbfrcpy.set(1)
    unpck_trnfrattr = unpck.parm('transfer_attributes')
    unpck_trnfrattr.set('x')
    attrbtwrnglaftupsnpk = attrbwrngl_aftunpck.parm('snippet')
    attrbtwrnglaftupsnpk.set('@Cd=v@x;')
    attrbwrngl_aftunpck_gp = attrbwrngl_aftunpck.parm('group')
    attrbwrngl_aftunpck_gp.set('sysK')
    hou.hda.installFile('/SCORPION/PYTHON/TREE_PAINTING/imp/SideFX__deciduoustree.otl'
                        )

    my_otl = obj_ctxt.createNode('SideFX::deciduoustree')
    my_otl_treegen = my_otl.parm('treesys1_lsystem1_generations')
    my_otl_treegen.set(6)
    x = hou.node('/obj/deciduoustree1/treesys1/OUT')
    y = x.path()
    z = str(y)
    objmrg_pth = objmrg.parm('objpath1')
    objmrg_pth.set(z)

    # vopsop
    # create node

    vopout = vopsopptcd.createNode('output')
    vopcmap = vopsopptcd.createNode('parameter')
    vopuv = vopsopptcd.createNode('parameter')
    vopvectfloat = vopsopptcd.createNode('vectofloat')
    vopcolormap = vopsopptcd.createNode('colormap')

    # set input

    vopvectfloat.setInput(0, vopuv)
    vopcolormap.setInput(0, vopcmap)
    vopout.setInput(8, vopcolormap)
    vopcolormap.setInput(1, vopvectfloat, 0)
    vopcolormap.setInput(2, vopvectfloat, 1)
    vopsopptcd.layoutChildren()

    # set parm

    vopclrmapwrap = vopcolormap.parm('wrap')
    vopclrmapwrap.set('Streak')
    vopcmap_parname = vopcmap.parm('parmname')
    vopcmap_parname.set('cmap')
    vopcmap_parmlb = vopcmap.parm('parmlabel')
    vopcmap_parmlb.set('Color Map')
    vopcmap_parmtype = vopcmap.parm('parmtype')
    vopcmap_parmtype.set(17)
    vopuv_parname = vopuv.parm('parmname')
    vopuv_parname.set('uv')
    vopuv_parmlb = vopuv.parm('parmlabel')
    vopuv_parmlb.set('uv')
    vopuv_parmtype = vopuv.parm('parmtype')
    vopuv_parmtype.set(6)
    mrg.setDisplayFlag(True)
    my_otl.setDisplayFlag(False)
    obj_ctxt.layoutChildren()

			