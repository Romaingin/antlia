from ..blueprint.rectangle import Rectangle
from ..blueprint.text import Text
from ..blueprint.primitive import font_manager
from .element import Element
from .color import Color, lighthen
from .const import *

class Label(Element):
	def __init__(self, name):
		super(Label, self).__init__(name)
		self.type = "label"
		
		# Specific to the Button element
		self.attributes = {
			"label": name,
			"drag-window": False,
			"background-color": "none",
			"font": "lato-light",
			"text-color": "dark-grey",
			"text-align": "left",
			"text-size": 12,
			"padding": "0px"
		}

	def build(self, renderer, rect):
		self._clearBlueprint()
		colors = {
			"background-color": Color[self.attributes["background-color"]],
			"text-color": Color[self.attributes["text-color"]]
		}

		# Apply padding
		text_rect = rect.getPaddingRect(self.attributes["padding"])

		# Bluid blueprint
		if colors["background-color"] is not None:
			R = Rectangle(0.0, 0.0, 1.0, 1.0)
			R.build(renderer, rect, colors["background-color"])
			self.blueprint.append(R)

		x = 0.0
		if self.attributes["text-align"] == "center":
			x = 0.5
		elif self.attributes["text-align"] == "right":
			x = 1.0
		T = Text(x, 0.5,
				self.attributes["label"],
				self.attributes["font"],
				self.attributes["text-size"],
				align=self.attributes["text-align"])

		T.build(renderer, text_rect, colors["text-color"])
		# print(font_manager.getGlyphFromChar(T.getFontId(), "H").advance)
		self.blueprint.append(T)
