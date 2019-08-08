n = nuke.toNode('TransformGeo1')
		
k = n.knob('translate').getValue()
		
x = k[0]
xAdjusted = x +0.01
		
k = n.knob('translate').setValue(xAdjusted, 0)