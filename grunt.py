import math


def lobster_back_bend(DM,CT,DV,ST,BD,HV):
	radius = DM // 2
	angle = 360 / DV
	parts = int(90 / angle)
	throat = CT - radius
	base_len = CT + radius
	pattern = round(math.pi * (DM-ST))
	stype = (HV-2) // 2
	A, B = [], []
	n = 0

	for _ in range(parts):
		x = math.sin(math.radians(n))
		spaces = round(x * radius)
		A += [CT + spaces]
		B += [CT - spaces]
		n += angle

	plan_spaces = [base_len] + A[::-1] + B[1:] + [throat]
	new_angle = BD / HV
	A = 'Length = {}'.format(pattern)
	return A + "\n" + ''.join(str(i) + ' = ' + str(round(math.tan(math.radians(new_angle)) * x)) + "\n" for i,x in enumerate(plan_spaces))


def branch_piece(BD,DV):
    branch_radius = BD // 2
    angle = 360 / DV
    parts = int(90 // angle)

    # BRANCH PIPE SPACES FOR TRIANGULATION
    A = []
    n = 0
    for _ in range(parts+1):
        x = math.sin(math.radians(n))
        spaces = round(x * branch_radius)
        A.append(spaces)
        n += angle
    return A


# 90 DEGREE BRANCH HEIGHTS ON MAIN PIPE NOT INCLUDING BRANCH LENGTH
def traversed_heights(B, main_pipe_radius):
    t_heights = [round(main_pipe_radius - (((main_pipe_radius**2) - (i**2)) **.5)) for i in B]
    return t_heights


def angle_branch(MD,BD,SL,BA,DV,ST):
    main_pipe_radius = MD // 2
    B = branch_piece(BD,DV)
    X = traversed_heights(B,main_pipe_radius)
    branch_radius = B[-1]
    branch_spaces = []
    for n in B:
        branch_spaces += [branch_radius - n]
        branch_spaces += [branch_radius + n]

    # CENTRE HEIGHTS
    mid_heights = [z / math.tan(math.radians(BA)) for z in sorted(branch_spaces[1:])]

    # LOW HEIGHTS
    Y = X + X[-2::-1]
    low_heights = [z / math.sin(math.radians(BA)) for z in Y]

    # FINAL TOTAL HEIGHTS
    final_lengths = [round(a + b + SL) for a,b in zip(mid_heights, low_heights)]

    #pattern = round(math.pi * (BD-ST))
    A = 'Length = {}'.format(round(math.pi * (BD-ST)))
    return A + "\n" + ''.join(str(i) + ' = ' + str(v) + "\n" for i,v in enumerate(final_lengths))

