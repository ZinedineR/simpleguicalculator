# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 348,332 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.but1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer3.Add( self.but1, 0, wx.ALL, 5 )
		
		self.but2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer3.Add( self.but2, 0, wx.ALL, 5 )
		
		self.but3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer3.Add( self.but3, 0, wx.ALL, 5 )
		
		self.butPlus = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer3.Add( self.butPlus, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.but4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer4.Add( self.but4, 0, wx.ALL, 5 )
		
		self.but5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer4.Add( self.but5, 0, wx.ALL, 5 )
		
		self.but6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer4.Add( self.but6, 0, wx.ALL, 5 )
		
		self.butMin = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer4.Add( self.butMin, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.but7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer5.Add( self.but7, 0, wx.ALL, 5 )
		
		self.but8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer5.Add( self.but8, 0, wx.ALL, 5 )
		
		self.but9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer5.Add( self.but9, 0, wx.ALL, 5 )
		
		self.butDiv = wx.Button( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer5.Add( self.butDiv, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.butPeriod = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer6.Add( self.butPeriod, 0, wx.ALL, 5 )
		
		self.but0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer6.Add( self.but0, 0, wx.ALL, 5 )
		
		self.solveButton = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer6.Add( self.solveButton, 0, wx.ALL, 5 )
		
		self.butMultiply = wx.Button( self, wx.ID_ANY, u"*", wx.DefaultPosition, wx.Size( 35,35 ), 0 )
		bSizer6.Add( self.butMultiply, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Inputan" ), wx.VERTICAL )
		
		self.text = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY )
		sbSizer1.Add( self.text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.clearButton = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.clearButton, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.m_menu31 = wx.Menu()
		self.m_menu3.AppendSubMenu( self.m_menu31, u"MyMenu" )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem3 )
		
		self.m_menubar2.Append( self.m_menu3, u"MyMenu" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.but1.Bind( wx.EVT_BUTTON, self.addText )
		self.but2.Bind( wx.EVT_BUTTON, self.addText )
		self.but3.Bind( wx.EVT_BUTTON, self.addText )
		self.butPlus.Bind( wx.EVT_BUTTON, self.addText )
		self.but4.Bind( wx.EVT_BUTTON, self.addText )
		self.but5.Bind( wx.EVT_BUTTON, self.addText )
		self.but6.Bind( wx.EVT_BUTTON, self.addText )
		self.butMin.Bind( wx.EVT_BUTTON, self.addText )
		self.but7.Bind( wx.EVT_BUTTON, self.addText )
		self.but8.Bind( wx.EVT_BUTTON, self.addText )
		self.but9.Bind( wx.EVT_BUTTON, self.addText )
		self.butDiv.Bind( wx.EVT_BUTTON, self.addText )
		self.butPeriod.Bind( wx.EVT_BUTTON, self.addText )
		self.but0.Bind( wx.EVT_BUTTON, self.addText )
		self.solveButton.Bind( wx.EVT_BUTTON, self.solveFunc )
		self.butMultiply.Bind( wx.EVT_BUTTON, self.addText )
		self.clearButton.Bind( wx.EVT_BUTTON, self.clearFunc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addText( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def solveFunc( self, event ):
		event.Skip()
	
	
	def clearFunc( self, event ):
		event.Skip()
	

