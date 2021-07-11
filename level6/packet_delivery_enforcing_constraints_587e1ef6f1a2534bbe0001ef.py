"""
https://www.codewars.com/kata/587e1ef6f1a2534bbe0001ef
Description:
"Create class "Package" that represents a package which has a length, width, height (cm) and weight (kg) parameter.
Furthermore, the following should always give the current volume of the package:
p = Package(0.2, 0.2, 0.2)
p.volume  # computes 0.2 * 0.2 * 0.2 and returns it
But lo and behold! The following constraints must be satisfied for all packages at all time:
0 < length <= 350
0 < width <= 300
0 < height <= 150
0 < weight <= 40
For example, the following should raise a custom (written-by-you) DimensionsOutOfBoundError:
p = Package(351, 0.2, 0.2, 0.2)
# raises DimensionsOutOfBoundError with  message:
#  "Package length==351 out of bounds, should be: 0 < length <= 350"
Assignments with out-of-bounds values also produce the same error:
p = Package(10, 0.2, 0.2, 0.2)
p.length = 351
# raises DimensionsOutOfBoundError with  message:
#  "Package length==351 out of bounds, should be: 0 < length <= 350"
Notes
The error message given when "DimensionsOutOfBoundError" is raised should always follow the exact format:
"Package {variable}=={value} out of bounds, should be: {lower} < {variable} <={upper}"
where variable is length, width, height or weight;
value is the out-of-bounds value and lower/upper are lower/upper bound on the variable, respectively".
"""

class Package:

    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, l):
        self._length = self._assess_value('length', l)

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, w):
        self._width = self._assess_value('width', w)

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, h):
        self._height = self._assess_value('height', h)

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, wt):
        self._weight = self._assess_value('weight', wt)

    @property
    def volume(self):
        return self._length * self._width * self._height

    def __init__(self, l, w, h, wt):
        self.length = l
        self.width = w
        self.height = h
        self.weight = wt

    def _assess_value(self, measure_name, measure_value):
        limits_dict = {'length': (0, 350), 'width': (0, 300), 'height': (0, 150), 'weight': (0, 40)}
        curr_limits = limits_dict.get(measure_name, ())
        if not curr_limits[0] < measure_value <= curr_limits[1]:
            raise DimensionsOutOfBoundError(measure_name, measure_value, curr_limits)
        return measure_value


class DimensionsOutOfBoundError(Exception):

    def __init__(self, measure_name, measure_value, limits):
        doobe_message = f"Package {measure_name}=={measure_value} out of bounds, should be: " \
               f"{limits[0]} < {measure_name} <= {limits[1]}"
        super().__init__(doobe_message)


"""alternative solutions: https://www.codewars.com/kata/587e1ef6f1a2534bbe0001ef/solutions/python"""

"""solution by ZozoFouchtra:"""

class PackageAlt1(object):
    # my comment: might be good practice: lower_limits = {"length": 0, "width": 0, "height": 0, "weight": 0}
    upper_limits = {"length": 350, "width": 300, "height": 150, "weight": 40}

    def __init__(self, l, w, h, wg):
        self.length = l
        self.width = w
        self.height = h
        self.weight = wg

    def __setattr__(self, measure, measure_value):
        if measure_value <= 0 or measure_value > self.upper_limits[measure]:
            raise DimensionsOutOfBoundErrorAlt1(measure, measure_value, self.upper_limits[measure])
        self.__dict__[measure] = measure_value

    @property
    def volume(self):
        return self.length * self.width * self.height


class DimensionsOutOfBoundErrorAlt1(Exception):
    def __init__(self, measure, measure_value, upper_limit):
        self.str = f"Package {measure}=={measure_value} out of bounds, should be: 0 < {measure} <= {upper_limit}"

    def __str__(self):
        return self.str


"""solution by Blind4Basics:"""

class DimensionsOutOfBoundErrorAlt2(Exception):
    pass


class PackageAlt2(object):
    LIMITS = {'length': (0, 350), 'width': (0, 300), 'height': (0, 150), 'weight': (0, 40)}

    def __init__(self, *args):
        self.length, self.width, self.height, self.weight = args

    @property
    def volume(self):
        return self.length * self.width * self.height

    def __setattr__(self, measure, measure_value):
        min_limit, max_limit = self.LIMITS[measure]
        if not (min_limit < measure_value <= max_limit):
            raise DimensionsOutOfBoundError(
                f"Package {measure}=={measure_value} out of bounds, "
                f"should be: {min_limit} < {measure} <= {max_limit}"
            )
        self.__dict__[measure] = measure_value
