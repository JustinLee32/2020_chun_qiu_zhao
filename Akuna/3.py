def find_intersections(c_x, c_y, c_z, c_r,
					   ray_x, ray_y, ray_z, dir_x, dir_y, dir_z):
	"""
	Args:
		c_x, c_y, c_z (float): coordinates of center point of the sphere.
		c_r (float): radius of the sphere.
		ray_x, ray_y, ray_z (float): coordinates of the origin of the ray.
		dir_x, dir_y, dir_z (float): direction vector of the ray.
	
	Returns:
		[] or list of floats
		
	"""
	# Write your code here
	res=[]
	A=dir_x**2+dir_y**2+dir_z**2
	B=2*(ray_x-c_x)*dir_x+2*(ray_y-c_y)*dir_y+2*(ray_z-c_z)*dir_z
	C=(ray_x-c_x)**2+(ray_y-c_y)**2+(ray_z-c_z)**2-c_r**2
	delta=B**2-4*A*C
	if delta<0:
		return [0.0]
	elif delta==0:
		t=-B/(2*A)
		if t>=0:
			d=math.sqrt(dir_x**2*t**2+dir_y**2*t**2+dir_z**2*t**2)
			res.append(d)
		if not res:
			res.append(0.0)
		return res
	elif delta>0:
		t1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
		t2=(-B-math.sqrt(B**2-4*A*C))/(2*A)
		if t1>=0:
			d=math.sqrt(dir_x**2*t1**2+dir_y**2*t1**2+dir_z**2*t1**2)
			res.append(d)
		if t2>=0:
			d=math.sqrt(dir_x**2*t2**2+dir_y**2*t2**2+dir_z**2*t2**2)
			res.append(d)
		if not res:
			res.append(0.0)
		res.sort()
		return res
