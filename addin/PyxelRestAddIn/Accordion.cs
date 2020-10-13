using System;
using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Windows.Forms.Layout;

namespace Opulos.Core.UI {

// Version 2015.08.18
// -Added code to eliminate scrollbar flicker when sliding
//  open for a nested accordion.
// -Fixed a issue with the fill down button  not working if
//  the control is not locked. The control is now temporarily
//  locked, a layout is performed, and then the original lock
//  value is restored.
// -Fixed issue with the fill down button not scrolling the
//  control to the ideal spot.
// -Added Refresh() after control close animation, otherwise
//  scrollbar artifacts would be left on the screen.
// -Fixed Fill-All button from being enabled when it has no
//  effect. Also, fixed problem will allocating the wrong
//  extra space.
// -ToolBox Open-All button is now disabled if the accordion's
//  OpenOneOnly is true.
// 
// Version 2015.08.05
// -Fixed bug when FillModeGrowOnly is true. The extra height
//  was incorrectly being reset to zero for all controls.
// -When ResetFillOnCollapse is true, the controls are now
//  unlocked also. Otherwise a locked control with a fillWt > 0
//  would appear much smaller next time it is opened.
// -Now, resize bars do not fade-in when the mouse is over a
//  a header checkbox.
// -Improved open animation, especially for controls at the
//  bottom of the screen. Before, the animation would occur
//  below the visible region. Now the control is moved up
//  and then the animation happens.
// 
// Version 2015.08.03
// -Improved layout handling. Removed the internal FlowLayoutPanel
//  and replaced with a custom AccordionLayoutEngine. This
//  eliminates the problem where the horizontal scrollbar is
//  briefly displayed when the vertical scrollbar first appears.
// -Added an option for slide-up and slide-down animation effects
//  when a control is opened or closed.
// -Added an option to show a resize bar, which acts a visual cue
//  for the user to know the control can be resized.
// -The resize bars are set by default to fade-in and fade-out
//  based on the proximity of the mouse pointer. Set the
//  proximity threshold to zero to always show the resize bars.
// -Resize bars can be moved using the up and down arrow keys.
// -Fixed methodology to set the focus on the first control when
//  a checkbox is opened.
// -Support added for adhering to the added control's Minimimum
//  and Maximum size properties.
// 
// Version 2015.04.05
// -Removed unused line of code: bool hit = bounds.Contains(pt);
// -Fixed bug when the mouse was clicked on a drag area which
//  was on top of a scrollbar. The scrollbar consumed the mouse
//  events and needed to have the capture released.
// -Fixed bug. Mouse would turn into the grab cursor when it
//  was over a grab bar that belonged to an Accordion in a
//  background window, or when the mouse was on top of a
//  child window that was covering the accordion.
// 
// Version 2015.01.16
// -Rewrote the mouse drag behavior using IMessageFilter. In
//  addition to cleaner code, this also fixed the mouse cursor
//  staying as the SizeNS cursor bug.
// -Added GrabWidth property that specifies when the mouse turns
//  into the GrabCursor cursor.
// -Added GrabCursor property, default value of Cursors.SizeNS.
// -Added <summary> comments to the properties and input parameters.
// -Fixed layout issue that happens when minimizing and restoring
//  a window. Some of the controls would appear invisible because
//  as the form is minimized, its height changes to zero.
//  For more info, see the Accordion.OnSizeChanged method and the
//  AccordionLayoutProblemForm at the bottom.
// -Fixed the bug when the accordion font changes, the tool box's
//  sub-menu fonts weren't updated.
//  Before the font size would stay the same for the sub-menus.
// -Fixed fill all from being greyed out. It was using the
//  wrong size.
// -Overrode the Accordion's GetPreferredSize method to return
//  the FLP host's preferred size.
// -Added method CheckBoxForControl(Control c) which returns the
//  header checkbox for a given nested control, or null if the
//  control is not found.
// 
// v2014.11.12
// -Initial Release

///<summary>Use the Add(Control, "Title") method to add controls to the accordion.
///
///<para>Brief explation of 'Extra Height': Extra height is calculated to be the difference
///of the accordion's height and the of the sum of all heights of the accordion's contents:
///header checkboxes, margins, paddings, and preferred size heights of added controls.
///If the difference is less than zero then any controls that can be smaller than their
///preferred height will decrease in height.</para>
///
///<para>There are two options how positive Extra Height can be allocated.</para>
///<para>1) Allocate all the extra height to the last opened checkbox with a fill weight > 0, or</para>
///<para>2) Allocate the extra height between the open controls based on their fill weights.</para>
///
///<para>The #2 option is likely better for most situations, and is the default value.
///The boolean property 'FillLastOpened' determines which mode is used, and its default
///value is false.</para>
///
///<para>Another feature of this Accordion is that it allows a control to be expanded by
///clicking and dragging the mouse. This is especially useful when using multiline
///textboxes. Instead of having to allocate a large number of preset visible lines,
///the textboxes can be added to an accordion and the user can increase the height
///of any textbox as needed by clicking and dragging in the grab area.</para>
///</summary>
public class Accordion : UserControl, IMessageFilter {

	///<summary>The factory used to create a resize bar when a control is added to an Accordion.
	///A resize bar acts as a visual cue for the user to know the corresponding control can be resized.</summary>
	public static IResizeBarFactory GlobalResizeBarFactory = new DefaultResizeBarFactory();

	///<summary>The factory used to create a header CheckBox when a control is added to an Accordion.
	///A default factory is provided.</summary>
	public static ICheckBoxFactory GlobalCheckBoxFactory = new DefaultCheckBoxFactory();

	///<summary>The glyph to prefix to a closed checkbox's text if the DownArrow member is null.
	///The default value is the unicode down arrow followed by two spaces.</summary>
	public static String GlobalDownArrow = "\u25bc  ";

	///<summary>The glyph to prefix to an open checkbox's text if the UpArrow member is null.
	///The default value is the unicode up arrow followed by two spaces.</summary>
	public static String GlobalUpArrow = "\u25b2  ";

	//---------------------------------------------
	// New variables for Accordion v2:

	///<summary>The duration of the animation in milliseconds when a control is opening. Note: the control is unresponsive during animation.
	///The default value is 300 milliseconds. Set to 0 to disable the animation.</summary>
	public int AnimateOpenMillis { get; set; }

	///<summary>The duration of the animation in milliseconds when a control is closing. Note: the control is unresponsive during animation.
	///The default value is 300 milliseconds. Set to 0 to disable the animation.</summary>
	public int AnimateCloseMillis { get; set; }

	///<summary>The animation effect to use when a control is opened. The value must consist of the Show flag plus one of the animation
	///effects (Center, Slide). If slide is used, then a direction flag is required. The default value is Show | Slide | VerticalPositive.
	///Set to None to disable the animation.</summary> 
	public AnimateWindowFlags AnimateOpenEffect { get; set; }

	///<summary>The animation effect to use when a control is closed. The value must consist of the Hide flag plus one of the animation
	///effects (Center, Slide). If slide is used, then a direction flag is required. The default value is Hide | Slide | VerticalNegative.
	///Set to None to disable the animation.</summary>
	public AnimateWindowFlags AnimateCloseEffect { get; set; }

	///<summary>The Add control method provides a parameter to specify a resize grab bar. If the input value is null, then a resize bar is
	///added if AddResizeBars is true, fillWt > 0, and AllowMouseResize is true. The ResizeBarFactory is called to create the resize bar
	///control. The default value is true.</summary>
	public bool AddResizeBars { get; set; }

	///<summary>The distance between the mouse and the resize bar before the resize bar appears or vanishes. Set this value to 0
	///to disable the fade effects and always display the resize bar for open controls. The default value is 30 * (dpi / 120).</summary>
	public int ResizeBarsFadeProximity { get; set; }

	///<summary>The duration in milliseconds for the resize bar fade-in effect. The default value is 800 ms. Set to 0 to skip the fade effect.</summary>
	public int ResizeBarsFadeInMillis { get; set; }

	///<summary>The duration in milliseconds for the resize bar fade-out effect. The default value is 800 ms. Set to 0 to skip the fade effect.</summary>
	public int ResizeBarsFadeOutMillis { get; set; }

	///<summary>An option to keep the focus on the resize bar after a user resized a control. The default value is false, which means the
	///focus is put back on the previous control. For example, after resizing a multiline textbox, it is more convenient to have the focus
	///transfer back to the textbox. However, if the previous control is out of view, the resize bar keeps the focus if
	///ResizeBarsKeepFocusIfControlOutOfView is true.</summary>
	public bool ResizeBarsKeepFocusAfterMouseDrag { get; set; }

	///<summary>If a user clicks on a resize bar without dragging then it will keep the focus. The default value is true. If false, then the
	///focus is returned to the previous control. However, if the previous control is out of view, the resize bar keeps the focus if
	///ResizeBarsKeepFocusIfControlOutOfView is true.</summary>
	public bool ResizeBarsKeepFocusOnClick { get; set; }

	///<summary>An option to restore the focus to the previous control regardless if that control is viewable or not. The default value is true,
	///which means the resize bar keeps the focus if the previous control is not currently in the scrollbar viewport.</summary>
	public bool ResizeBarsKeepFocusIfControlOutOfView { get; set; }

	///<summary>Sets the TabStop property of the resize bars after they are created by the ResizeBarFactory. The default value is true.
	///This property is most useful when resize bars are always visible by setting ResizeBarsFadeProxity to zero.</summary>
	public bool ResizeBarsTabStop { get; set; }

	///<summary>An option keep the currently selected resize bar visible, even if the distance from the mouse exceeds the proximity value.
	///The default value is true.</summary>
	public bool ResizeBarsStayVisibleIfFocused { get; set; }

	///<summary>An option to have the vertical scrollbar move with the resize bar while it is being dragged with the mouse. The default value
	///is true. Note: This variable also applies when dragging and no resize bar was added.</summary>
	public bool ResizeBarsStayInViewOnMouseDrag { get; set; }

	///<summary>An option to have the vertical scrollbar move with the resize bar when an arrow key is pressed. The default value is true.</summary>
	public bool ResizeBarsStayInViewOnArrowKey { get; set; }

	///<summary>When the up arrow or down arrow key is pressed, the resize bar will increase or decrease its position by this amount.
	///The default value is 10. Set to 0 to disable using the arrow keys.</summary>
	public int ResizeBarsArrowKeyDelta { get; set; }

	///<summary>The default amount of space to set around a resize bar, if not explicitly set in the Add control method. The default value
	///is null, which means the value used will be the same as the content margin. Note: Large margins can cause the scrollbars to auto appear,
	///so the margin property is cached in a internal variable used by the layout engine.<summary>
	public Padding? ResizeBarsMargin { get; set; }

	///<summary>An option to automatically hide a resize bar when it is scrolled such that it is not completely visible.
	///Only applies when ResizeBarsFadeProximity is zero. The default value is false. Note: the resize bars are positioned
	///so that they are vertically centered over the bottom edge of the internal Control2 host. However, if a resize bar
	///is the bottom-most control, then it will be moved up if the Margin of Control2 cannot fit half the height of the
	///resize bar. Otherwise the overhanging part of the resize bar would increase the client height and cause the vertical
	///scrollbar to appear.</summary>
	public bool ShowPartiallyVisibleResizeBars { get; set; }

	///<summary>The amount of available space that the resize bars will expand. The default value is 1.0, which means a resize
	///bar will go from one side to the other, minus the resize bar margins.</summary>
	public double ResizeBarsFill { get; set; }

	///<summary>The position of the resize bar if the ResizeBarsFill is not 1.0. The default value is 0.5,
	///which means the resize bars are centered.</summary>
	public double ResizeBarsAlign { get; set; }

	///<summary>The minimum length that a resize bar is allowed to be. The default value is 50. If the ResizeBarsFillWeight
	///is zero, then the resize bars will be the minimum length.</summary>
	public int ResizeBarsMinimumLength { get; set; }

	///<summary>Specifies the ResizeBarFactory for this specific instance. The default value is null, which means the
	///GlobalResizeBarFactory is used.</summary>
	public IResizeBarFactory ResizeBarFactory { get; set; }

	///<summary>Accordion v2 uses a different underlying control than version 1, which handles DockStyle.Fill differently. Setting this
	///value to true will map the DockStyle for Anchor flags and set DockStyle to None.</summary>
	public bool AutoFixDockStyle { get; set; }

	///<summary>An option to never allow a control to go shorter than its preferred height. Many controls do not set a MinimumSize,
	///so their default MinimumSize is (0, 0), which means the user can decrease the size of the control so that it is no longer visible.
	///The default value is true, which makes the preferred height the minimum height allowed.</summary> 
	public bool ControlMinimumHeightIsItsPreferredHeight { get; set; }

	///<summary>An option to never allow a control to go narrower than its preferred width. Many controls do not set a MinimumSize,
	///so their default MinimumSize is (0, 0), which means the user can decrease the size of the control so that it is no longer visible.
	///The default value is true, which makes the preferred width the minimum width allowed. If false, then check boxes with long
	///text will break at white spaces and wrap underneath. It may be look nicer to provide a checkbox implementation that gradually
	///removes only the characters that cannot be displayed, rather than removing an entire 'word' at a time.
	///</summary>
	public bool ControlMinimumWidthIsItsPreferredWidth { get; set; }

	//---------------------------------------------

	///<summary>Specifies the CheckBoxFactory for this specific instance. The default value is null, which means the
	///GlobalCheckBoxFactory is used.</summary>
	public ICheckBoxFactory CheckBoxFactory { get; set; }

	///<summary>Allows at most one control to be expanded at a time. The previously opened control is automatically closed.
	///The default value is false.</summary>
	public bool OpenOneOnly { get; set; }

	///<summary>When a checkbox is closed, any extra space acquired (either by user resizing or growing) will be reset to
	///zero and the control will be set to unlocked. FillResetOnCollapse is usually true when FillLastOpened is true.
	///The default value is false.</summary>
	public bool FillResetOnCollapse { get; set; }

	///<summary>Specifies that extra height is strictly increasing and is not decreased (except by the user). Extra height is
	///accumulated by controls that have a fill weight > 0 and when the parent control increases in height.
	///The default value is false.</summary>
	public bool FillModeGrowOnly { get; set; }

	///<summary>The last eligible control that was opened receives all the extra height. The extra height that was previously
	///allocated to the previous control is removed. If FillLastOpened is true, then usually FillResetOnCollapse is also true.
	///The default value is false.</summary>
	public bool FillLastOpened { get; set; }

	///<summary>The default amount of space to set around a control (when it is the open state).
	///The total amount of space around a control is going to be the sum of ContentPadding + ContentMargin + ControlMargin.
	///The difference is that if ContentBackColor has a value, then the ContentPadding area will fill with that color,
	///where as the ContentMargin will appear empty. The default is 5 pixels on each side.</summary>
	///<seealso cref="ContentBackColor"/>
	public Padding? ContentPadding { get; set; }

	///<summary>Similar to ContentPadding, it specifies a default amount of space to add around a control. The default value is null.
	///See Content Padding for more information.</summary>
	public Padding? ContentMargin { get; set; }

	///<summary>The default amount of empty space to add around a checkbox. The default value is Padding.Empty. The margin is passed
	///to the CreateCheckBox method, and it is up to the CheckBoxFactory to set the checkbox's Margin property.</summary>
	public Padding? CheckBoxMargin { get; set; }

	///<summary>An option to automatically set the BackColor property of an added control. The default value is null.</summary>
	public Color? ControlBackColor { get; set; }

	///<summary>An option to automatically set the BackColor property of the content that is hosting an added control.
	///The ContentBackColor, together with ContentPadding, can be used to create a colored border around the control.
	///The default value is null.</summary>
	public Color? ContentBackColor { get; set; }

	///<summary>Specifies that the Accordion should expand to fill the width of its parent container if extra space is available.
	///The default value is true.</summary>
	public bool FillWidth { get; set; }

	///<summary>Specifies that the Accordion should expand to fill the height of its parent container if extra space is available.
	///The default value is true.</summary>
	public bool FillHeight { get; set; }

	///<summary>If FillWidth is true and the PreferredSize width is greater than the CientSize width, then the preferred width
	///is used for the layout if GrowAndShrink is false or ControlMinimumWidthIsItsPreferredWidth is true. Otherwise the
	///ClientSize width is used, which means controls will become narrower than their preferred widths.
	///If FillWidth is false and GrowAndShrink is true, then PreferredSize width is used for the layout, which means the
	///width of all controls will be the same as the widest checkbox or widest currently open control. If FillWidth is false
	///and GrowndShrink is also false, then the currently PreferredSize width is used if it is larger than any previous PreferredSize
	///width. For example, when a control is opened, it might require more width and a horizontal scrollbar might be displayed.
	///If GrowAndShrink is true, then when the control is closed, the display area will return to the previous size and the
	///scrollbars will vanish. If GrowAndShrink is false, then display area will remain the same, and the horizontal scrollbar
	///will stay. The default value is true.</summary>
	public bool GrowAndShrink { get; set; }

	///<summary>Gets or sets the text to prefix to the checkbox text when the content is hidden. The default value is null,
	///which means the GlobalDownArrow value is used.</summary>
	public String DownArrow { get; set; }

	///<summary>Gets or sets the text to prefix to the checkbox text when the content is visible. The default value is null,
	///which means the GlobalUpArrow value is used.</summary>
	public String UpArrow { get; set; }

	///<summary>Option to display a tool box when either the mouse is hovered over the rightmost side of an open checkbox header
	///or a right click on the header is made. The tool box contains buttons that allow the user the ability to control the height
	///of the control(s). The default value is true.</summary>
	public bool ShowToolMenu { get; set; }

	///<summary>Option to only display a tool box if a control has a fill weight greater than zero. The default value is false.</summary>
	public bool ShowToolMenuRequiresPositiveFillWeight { get; set; }

	///<summary>Option to display the tool box when the mouse is hovered over a closed checkbox header. The default value is false.</summary>
	public bool ShowToolMenuOnHoverWhenClosed { get; set; }

	///<summary>Option to display the tool box when the user right clicks on a checkbox header. The ShowToolMenu option must be true
	///for this to work. The default value is true.</summary>
	public bool ShowToolMenuOnRightClick { get; set; }

	///<summary>Specifies if the controls are in the open state when added. The default value is false.</summary>
	public bool OpenOnAdd { get; set; }

	///<summary>Insets put padding between the checkboxes and the edge of the accordion control. If you are using an ErrorProvider,
	///and setting an error message on a header checkbox, then the Insets should be 15 on the side where the error icon is shown.
	///The default value is zero for all sides.</summary>
	public Padding Insets {	get { return Padding; } set { Padding = value; }}

	///<summary>Option to allow the user to resize the content height of an open header by dragging the bottom of the content,
	///similar to a SplitContainer. Specify the drag activate region using the GrabWidth property. The default value is true.</summary>
	public bool AllowMouseResize { get; set; }

	///<summary>The width of the strip of pixels at the bottom of a control where a resize action can be activated.
	///The default value is 6 pixels. Note: If resize bars are added then the bounds of the resize bar control is the
	///grabbable area.</summary>
	public int GrabWidth { get; set; }

	///<summary>The cursor to display when a control's height can be resized by the user. The default value is Cursors.SizeNS.</summary>
	public Cursor GrabCursor { get; set; }

	///<summary>Specifies that the cursor should not activate unless a control's fill weight is greater than zero.
	///The default value is true.</summary>
	public bool GrabRequiresPositiveFillWeight { get; set; }

	//--------------------------------------------
	private List<Control> ResizeBarsList = new List<Control>();
	private List<Control2> Control2s = new List<Control2>();
	private bool isAnimating = false;
	private AccordionLayoutEngine layoutEngine = new AccordionLayoutEngine();
	private Control2 lastChecked = null; // used to track the last opened control so it can be closed if OpenOneOnly is true
	private ToolTip tips = new ToolTip();
	private ToolBox toolBox = new ToolBox();
	// used when OpenOneOnly is true. The previously open one is automatically closed which fires a checkedchanged event.
	// isAdjusting is used to ignore that event.
	private bool isAdjusting = false;

	// variables used for resizing:
	private const int WM_MOUSEMOVE = 0x0200;
	private const int WM_LBUTTONDOWN = 0x0201;
	private const int WM_LBUTTONUP = 0x0202;
	private const int WM_KEYDOWN = 0x100;
	private const int WM_SETREDRAW = 11;
	private const int WM_NCCALCSIZE = 0x83;
	private const int WM_NCPAINT = 0x85;
	private const int WM_ERASEBKGND = 0x14;
	private const int VK_UP = 0x26;
	private const int VK_DOWN = 0x28;
	private Control2 grabControl = null;
	private Point grabPoint = Point.Empty;
	private Point oldPoint = Point.Empty;
	private int originalDH = 0;
	private bool isDragging = false;
	private bool isOpening = false;
	private bool wasDragged = false;
	private bool origLocked = false;
	private bool resetLocked = true;
	private bool scrollToBottom = false;
	private Control resizeBarHiding = null;
	private Control2 currentControl2 = null; // used for arrow keys
	private IntPtr hwndPreviousFocus = IntPtr.Zero; // handle of window with previous focus before mouse down
	private bool ignoreNCCALCSIZE = false;
	private bool ignoreNCPAINT = false;
	//--------------------------------------------

	///<summary>
	///<para>Use the Add(Control, "Title") method to add controls to the accordion.</para>
	///<para>Use the Count property &amp; Control(i), CheckBox(i), ResizeBar(i) methods to access the controls.</para>
	///<para>Use the CheckBoxForControl(...) method to find the header checkbox for a particular control.</para>
	///<para>Use the Open &amp; Close methods to expand or collapse controls programmatically.</para>
	///<para>Use the UpArrow &amp; DownArrow properties to change the glyphs displayed.</para>
	///<para>Use the Insets property to set amount of empty space around the Accordion.</para>
	///<para>Use the ContentPadding &amp; ContentMargin properties to set the amount of empty space around a specific control.</para>
	///</summary>
	public Accordion() {
		AutoScroll = true;
		//AutoSize = true;
		AutoSizeMode = AutoSizeMode.GrowAndShrink;
		Dock = DockStyle.Fill;
		DoubleBuffered = true;
		//----------
		FillHeight = true;
		FillWidth = true;
		GrowAndShrink = true;
		ShowToolMenu = true;
		AllowMouseResize = true;
		ShowToolMenuOnHoverWhenClosed = false;
		ShowToolMenuOnRightClick = true;
		GrabCursor = Cursors.SizeNS;
		GrabRequiresPositiveFillWeight = true;
		CheckBoxMargin = Padding.Empty;
		//---------
		ControlMinimumHeightIsItsPreferredHeight = true;
		ControlMinimumWidthIsItsPreferredWidth = true;
		ResizeBarsKeepFocusOnClick = true;
		ResizeBarsKeepFocusIfControlOutOfView = true;
		ResizeBarsTabStop = true;
		ResizeBarsStayVisibleIfFocused = true;
		ResizeBarsStayInViewOnMouseDrag = true;
		ResizeBarsStayInViewOnArrowKey = true;
		AddResizeBars = true;
		AutoFixDockStyle = true;
		AnimateOpenMillis = 300;
		AnimateCloseMillis = 300;
		ResizeBarsFadeInMillis = 800;
		ResizeBarsFadeOutMillis = 800;
		ResizeBarsFill = 1.0;
		ResizeBarsAlign = 0.5;
		AnimateOpenEffect = AnimateWindowFlags.Show | AnimateWindowFlags.Slide | AnimateWindowFlags.VerticalPositive;
		AnimateCloseEffect = AnimateWindowFlags.Hide | AnimateWindowFlags.Slide | AnimateWindowFlags.VerticalNegative;
		//---------
		using (var g = Graphics.FromHwnd(IntPtr.Zero)) {
			float dpi = Math.Max(g.DpiX, g.DpiY);
			ResizeBarsFadeProximity = (int) (30 * (dpi / 120));
			GrabWidth = Math.Max(6, (int) (6 * (dpi / 120)));
			ContentPadding = new Padding(Math.Max(5, (int) (5 * (dpi / 120)))); // whitespace between edges
			ResizeBarsArrowKeyDelta = Math.Max(10, (int) (10 * (dpi / 120)));
			ResizeBarsMinimumLength = Math.Max(50, (int) (50 * (dpi / 120)));
		}
		//---------
		Application.AddMessageFilter(this);
	}

	protected override Point ScrollToControl(Control activeControl) {
		Point pt = this.AutoScrollPosition; // always maintain the current X value.
		if (isOpening) {
			pt.Y = base.ScrollToControl(activeControl).Y;
			if (scrollToBottom)
				pt.Y -= activeControl.Height;
		}
		else if (isDragging && ResizeBarsStayInViewOnMouseDrag && grabControl != null) {
			// changing the Visible property on the resize bars causes the scroll to jump up
			// to the active control. If the resize bar and active control are not seen on
			// at the same time, then this makes is so the resize bar cannot be grabbed.
			// Instead, maintain the current scroll position.
		
			// the resize bar should always be the active control at this point
			// there was a issue that was fixed that OpacityEx removing the pbox
			// transfered the focus to another contorl. So this code can act as
			// a safety net.
			if (grabControl.ResizeBar != null) {
				pt.Y = base.ScrollToControl(grabControl.ResizeBar).Y;
			}
			else {
				// no resize bar, need to manually adjust the point to scroll
				activeControl = grabControl;
				Point pt2 = base.ScrollToControl(activeControl);
				pt2.Y -= grabControl.Height;
				//return pt2;
				pt.Y = pt2.Y;
			}
		}

		return pt;
	}

	public class AddArgs {
		public Control c;
		public String text;
		public String toolTip;
		public double fillWt = 0;
		public bool? open;
		public Padding? contentPadding;
		public Padding? contentMargin;
		public Color? contentBackColor;
		public Padding? checkboxMargin;
		public Padding? resizeBarMargin;
		public bool? addResizeBar;
		public LayoutArgs layoutArgs;
		public Accordion Owner { get; internal set; }
		public CheckBox CheckBox { get; internal set; }
	}

	///<summary>
	///Parameters used during a PerformLayout operation to position and size a control.
	///All values are typically between 0.0 and 1.0.
	///</summary>
	public class LayoutArgs {
		///<summary>If extra horizontal space is available, then this value specifies how much of
		///that extra space is allocated to the width of the control. Typical values are either 0.0 or 1.0</summary>
		public double FillX = 0;

		///<summary>If extra vertical space is available, this this value specifies how much of
		///that extra space is allocated to the height of the control. Typical values are either 0.0 or 1.0</summary>
		public double FillY = 0;

		///<summary>If there is extra horizontal space available, then this value specifies where
		///to horizontally position the control. Typical values are either 0.0 (left justified), 0.5 (centered)
		///or 1.0 (right justified).</summary>
		public double AlignX = 0;

		///<summary>If there is extra vertical space available, then this value specifies where
		///to vertically position the control. Typical values are either 0.0 (top), 0.5 (middle)
		///or 1.0 (bottom).</summary>
		public double AlignY = 0;
	}

	///<summary>Adds a control to this accordion. A header CheckBox is displayed above the control with the specified text.</summary>
	///<param name="c">Required. The control to add. Note: If you want the control to expand then make sure c.DockStyle = DockStyle.Fill.</param>
	///<param name="text">Required. The text to display in the header checkbox.</param>
	///<param name="toolTip">Optional. The tooltip that is displayed when the mouse hovers over the checkbox header.</param>
	///<param name="fillWt">Optional. Specify a value greater than zero to have the control expand if there is extra height available.<br/>
	///There are two different modes:<br/>
	///<para>1) Extra height is allocated to a single control. The fillWt serves as a binary indicator (zero or positive).
	///All the extra height will be allocated to the last opened control that has a positive fill weight. All other
	///controls will appear at their preferred height. This mode is used when 'FillLastOpened' is true.</para>
	///<para>2) Extra height is distributed between open controls that have fillWt > 0 and are not locked by the user. The
	///extra height is allocated to these controls in proportion to their fillWt versus the sum of the fill weights.
	///This mode is used when 'FillLastOpened' is false.</para></param>
	///<param name="open">Optional. Specify if the control is initially opened or closed. If null, then this Accordion's 'OpenOnAdd' value is used.</param>
	///<param name="contentPadding">Optional. It overrides the 'ContentPadding' value for the added control only.</param>
	///<param name="contentMargin">Optional. It overrides the 'ContentMargin' value for the added control only.</param>
	///<param name="contentBackColor">Optional. It overrides the 'ContentBackColor' value for the added control only.</param>
	///<param name="checkboxMargin">Optional. It overrides the 'CheckBoxMargin' value for the added control only.</param>
	///<param name="addResizeBar">Optional. If null, then a resize bar is added if AddResizeBars is true, AllowMouseResize is true, and either fillWt > 0 or GrabRequiresPositiveFillWeight is false.</param>
	///<param name="resizeBarMargin">Optional. The amount of space to set around the resize bar. If null, then the content margin is used.</param>
	///<param name="layoutArgs">Optional. If c.Dock and c.Anchor are both None, then LayoutArgs is used to align and fill 'c' within the available area. All values in range [0.0, 1.0]</param> 
	///<returns>Returns the CheckBox header created by the CheckBoxFactory.</returns>
	public CheckBox Add(Control c, String text, String toolTip = null, double fillWt = 0, bool? open = null, Padding? contentPadding = null, Padding? contentMargin = null, Color? contentBackColor = null, Padding? checkboxMargin = null, bool? addResizeBar = null, Padding? resizeBarMargin = null, LayoutArgs layoutArgs = null) {
		AddArgs args = new AddArgs();
		args.c = c;
		args.text = text;
		args.toolTip = toolTip;
		args.fillWt = fillWt;
		args.open = open;
		args.contentPadding = contentPadding;
		args.contentMargin = contentMargin;
		args.contentBackColor = contentBackColor;
		args.checkboxMargin = checkboxMargin;
		args.addResizeBar = addResizeBar;
		args.resizeBarMargin = resizeBarMargin;
		args.layoutArgs = layoutArgs;
		return Add(args);
	}

	///<summary>Same as the other Add method, except the inputs are encapsulated in an object.</summary>
	public CheckBox Add(AddArgs args) {
		args.Owner = this;
		Control c = args.c;
		String toolTip = args.toolTip;
		double fillWt = args.fillWt;
		bool? open = args.open;
		Padding? contentPadding = args.contentPadding;
		Padding? contentMargin = args.contentMargin;
		Color? contentBackColor = args.contentBackColor;
		Padding? checkboxMargin = args.checkboxMargin;
		Padding? resizeBarMargin = args.resizeBarMargin;
		bool? addResizeBar = args.addResizeBar;
		LayoutArgs layoutArgs = args.layoutArgs;

		ICheckBoxFactory cbf = CheckBoxFactory ?? GlobalCheckBoxFactory;
		bool check = open.HasValue ? open.Value : OpenOnAdd;
		CheckBox cb = cbf.CreateCheckBox(args.text, check, Get(checkboxMargin, CheckBoxMargin));
		args.CheckBox = cb;

		// the unicode arrows cause a brief flicker of the scrollbar
		cb.Text = (cb.Checked ? GetUpArrow() : GetDownArrow()) + cb.Text;

		if (!addResizeBar.HasValue) {
			addResizeBar = AddResizeBars && AllowMouseResize && (fillWt > 0 || !GrabRequiresPositiveFillWeight);
		}

		if (AutoFixDockStyle && c.Dock != DockStyle.None) {
			c.Anchor = Map(c.Dock);
			c.Dock = DockStyle.None;
			// turn off AutoSize because the Control2 usercontrol will use the Control's
			// GetPreferredSize() method to override what bounds the AccordionLayoutEngine sets.
			c.AutoSize = false;
		}

		Control resizeBar = null;
		Padding c2Padding = Get(contentPadding, ContentPadding);
		Padding c2Margin = Get(contentMargin, ContentMargin);

		if (addResizeBar.Value) {
			Padding rbMargin = c2Margin;

			if (resizeBarMargin.HasValue)
				rbMargin = resizeBarMargin.Value;
			else if (ResizeBarsMargin.HasValue)
				rbMargin = ResizeBarsMargin.Value;

			var rbf = (ResizeBarFactory != null ? ResizeBarFactory : GlobalResizeBarFactory);
			resizeBar = (rbf != null ? rbf.CreateResizeBar(rbMargin) : null);
		}

		Control2 c2 = new Control2(cb, c, resizeBar, fillWt, layoutArgs);
		c2.Padding = c2Padding;
		c2.Margin = c2Margin;
		Control2s.Add(c2);

		if (contentBackColor.HasValue)
			c2.BackColor = contentBackColor.Value;
		else if (ContentBackColor.HasValue)
			c2.BackColor = ContentBackColor.Value;

		if (ControlBackColor.HasValue)
			c.BackColor = ControlBackColor.Value;

		if (!String.IsNullOrEmpty(toolTip)) {
			//tips.Add(cb, toolTip);
			tips.SetToolTip(cb, toolTip);
		}

		// adding controls fires a Layout event on the host which causes
		// the host height to increase because new controls are added.
		// If other controls are currently filling the space, then the
		// scrollbars would briefly appear before the controls are resized
		isAdjusting = true;
		Controls.Add(cb);

		if (resizeBar != null) {
			// add resizeBar before adding c2 so that the resize bar appears on top
			Controls.Add(resizeBar);
			ResizeBarsList.Add(resizeBar);
			resizeBar.TabStop = ResizeBarsTabStop;
			resizeBar.Visible = (ResizeBarsFadeProximity == 0 && open.HasValue && open.Value);
			resizeBar.Cursor = GrabCursor;
			resizeBar.GotFocus += delegate {
				currentControl2 = c2;
			};
			resizeBar.LostFocus += delegate {
				currentControl2 = null;
				// if the resize bar is losing its focus because it is hiding
				// then the unwanted default behavior is that the first checkbox
				// is selected, which can cause unwanted scrolling. To prevent this,
				// the focus is explicitly tranfered to the control. If the
				// focus was lost because of a mouse click or tab key, then let the
				// focus transfer naturally.
				if (resizeBar == resizeBarHiding) {
					RestoreFocus(c);
				}
				else {
					if (ResizeBarsFadeProximity > 0) {
						Point pt = Cursor.Position;
						Point pt2 = PointToClient(pt); // relative to this Accordion
						FadeResizeBars(pt2, pt);
					}
				}
			};
		}
		Controls.Add(c2);
		if (resizeBar != null) {
			// resize bars appear at the bottom, so it's more consistent to tab from
			// checkbox to control to resize bar.
			int x = c2.TabIndex;
			c2.TabIndex = resizeBar.TabIndex;
			resizeBar.TabIndex = x;
		}
		isAdjusting = false;

		cb.MouseHover += delegate {
			bool stm = ShowToolMenu && (c2.fillWt > 0 || !ShowToolMenuRequiresPositiveFillWeight);
			if (stm && !toolBox.Visible && (cb.Checked || ShowToolMenuOnHoverWhenClosed)) {
				var p1 = cb.PointToClient(Control.MousePosition);
				// must use pref-w because width is not accurate until first show
				int w = toolBox.GetPreferredSize(Size.Empty).Width + 1;
				if (p1.X >= cb.Width - w) {
					Point p = new Point { X = cb.Width - w, Y = cb.Height };
					toolBox.Current = c2;
					toolBox.Show(cb, p);
				}
			}
		};

		cb.MouseUp += (o, e) => {
			bool stm = ShowToolMenu && (c2.fillWt > 0 || !ShowToolMenuRequiresPositiveFillWeight);
			if (stm && e.Button == MouseButtons.Right && ShowToolMenuOnRightClick) {
				var p1 = cb.PointToClient(Control.MousePosition);
				int w = toolBox.Width;
				p1.X -= w/2;
				p1.Y -= w/2;
				toolBox.Current = c2;
				toolBox.Show(cb, p1);
			}
		};

		cb.MouseLeave += delegate {
			if (toolBox.Visible) {
				// since toolBox has no parent, its bounds are in screen coordinates
				if (!toolBox.Bounds.Contains(Control.MousePosition))
					toolBox.Hide();
			}
		};

		Action<bool> layout = (ControlAdded) => {
			bool b = cb.Checked;
			if (b) {
				c2.lastClicked = DateTime.Now;
				if (OpenOneOnly && lastChecked != null && c2 != lastChecked) {
					isAdjusting = true;
					lastChecked.cb.Checked = false;
					isAdjusting = false;
				}
				lastChecked = c2;
			}

			InternalPerformLayout();

			if (VerticalScroll.Visible) {
				var r1 = new RECT();
				var r2 = new RECT();
				GetWindowRect(Handle, out r2);

				if (cb.Checked) {
					GetWindowRect(c2.Handle, out r1);
					if (r1.Bottom > r2.Bottom) {
						isOpening = true;
						scrollToBottom = true;
						ScrollControlIntoView(c2);
						scrollToBottom = false;
						ScrollControlIntoView(cb);
						isOpening = false;
					}
				}
				else {
					// if checkbox is closed, then only need to
					// scroll to the bottom of the checkbox.
					GetWindowRect(cb.Handle, out r1);

					if (r1.Bottom > r2.Bottom) {
						isOpening = true;
						scrollToBottom = true;
						ScrollControlIntoView(cb);
						scrollToBottom = false;
						isOpening = false;
					}
				}
			}
		};

		cb.CheckedChanged += delegate {
			bool b = cb.Checked;

			String downArrow = GetDownArrow();
			String upArrow = GetUpArrow();
			String text = cb.Text;
			isAnimating = true;
			if (b) {
				if (text.StartsWith(downArrow))
					text = text.Substring(downArrow.Length);
				text = upArrow + text;
			}
			else {
				if (text.StartsWith(upArrow))
					text = text.Substring(upArrow.Length);
				text = downArrow + text;
				// must call FadeOut because a FadeIn might currently be in
				// progress. If simply c2.ResizeBar.Visible = false, then the
				// FadeIn() will finish after and make the resize bar visible.
				if (c2.ResizeBar != null)
					c2.ResizeBar.FadeOut(0);

				// if a control is closed, then reset its dh value to zero
				if (FillResetOnCollapse) {
					c2.dh = 0;
					c2.isLocked = false;
				}
			}

			cb.Text = text; // must set text regardless of isAdjusting
			isAnimating = false;

			// isAdjusting is true when multiple controls are being opened or closed
			// at the same time. The animation and layout are skipped. The layout will
			// be performed after all controls are opened or closed.
			if (isAdjusting) {
				c2.Visible = b;
				return;
			}

			if (b && AnimateOpenEffect != AnimateWindowFlags.None && AnimateOpenMillis > 0) {
				c2.lastClicked = DateTime.Now;
				if (OpenOneOnly && lastChecked != null && c2 != lastChecked) {
					isAdjusting = true;
					lastChecked.cb.Checked = false;
					isAdjusting = false;
				}
				lastChecked = c2;

				// if vertical scrollbars appear or increase, then a buffer space needs to be
				// maintained in order to scroll to the expanded control.
				int max1 = (VerticalScroll.Visible ? VerticalScroll.Maximum : 0);

				// step 1:
				// turn off screen updating and set c2.Visible to true. If this is not done,
				// then controls that have never been shown before appear animated as as a
				// 150x150 gray rectangle.
				SendMessage(this.Handle, WM_SETREDRAW, false, 0);
				//--------
				// for nested accordions, it was very observable that setting c2.Visible = true would
				// sometimes briefly cause scrollbars. Opening and closing the same checkbox header over
				// and over would sometimes cause WndProc messages to fire, and sometimes many clicks
				// in a row with no events. It seems like the NCCALCSIZE is causing the scrollbars to
				// to appear briefly. Setting the sizes to zero and then ignoring the NCCALCSIZE message
				// seems to do a good job at preventing the scrollbars from briefly appearing.
				isAnimating = true;
				c2.c.Size = Size.Empty;
				c2.Size = Size.Empty;
				ignoreNCCALCSIZE = true;
				c2.Visible = true;
				ignoreNCCALCSIZE = false;
				isAnimating = false;
				//--------
				// step 2:
				// Call InternalPerformLayout(). This create space for the control to slide into.
				// Set noPaint to true, otherwise sometimes an intermediate scrollbar is painted and
				// erased and then painted again.
				ignoreNCPAINT = true;
				var tma = InternalPerformLayout();

				// no more layouts wanted, so set isAnimating to true.
				isAnimating = true;

				// Determine if scrollbars have appeared or increased:
				int max2 = (VerticalScroll.Visible ? VerticalScroll.Maximum : 0);
				bool holdSpace = (max2 > max1);
				Padding mOrig = Padding.Empty;

				if (holdSpace) {
					// this is done otherwise the animation would appear below the visible region
					// maybe there is a better way to hold the space?
					// Tried adding a new Control() and setting the bounds to the
					// current bounds of the Control2, but it had the side effect that
					// it would trigger scrollbars to appear briefly (even though screen
					// updating is turned off).
					RECT r1 = new RECT();
					RECT r2 = new RECT();
					GetWindowRect(c2.Handle, out r1);
					GetWindowRect(Handle, out r2);

					// only need to scroll down if c2 is below the visible area of the accordion
					if (r1.Bottom > r2.Bottom) {
						mOrig = cb.Margin;
						Padding m = mOrig;
						m.Bottom += c2.Height + c2.Margin.Vertical;
						cb.Margin = m;

						// get the scrollbar value in the right location:
						isOpening = true;
						scrollToBottom = true;
						ScrollControlIntoView(c2);
						scrollToBottom = false;
						ScrollControlIntoView(cb);
						isOpening = false;
					}
					else
						holdSpace = false;
				}

				// step 3:
				// Hide the control again, otherwise the animation won't work if the control is
				// currently visible. ShowWindow(IntPtr, 0) is used because it has less overhead.
				//ShowWindow(c2.Handle, 0); // seems to cause unwanted painting (scrollbar flicker)
				c2.Visible = false;
				ignoreNCPAINT = false;
				//if (holdSpace) {} // used to do scrollToBottom here, but seems combined above is OK too

				// step 4:
				// Turn screen updating back on and call tma.Refresh(). There is a blank area
				// ready for the slide-down animation. The top-most accordion (tma) is refreshed.
				// Opening a checkbox in a nested accordion will push the controls in the
				// parent accordion downwards.
				SendMessage(this.Handle, WM_SETREDRAW, true, 0);
				tma.Refresh(); // required to repaint the new positions of the controls
				// step 5:
				// Call the animate function. But wait! First cache the index of c2 because for
				// some reason the AnimateWindow function sets the child control to index 0,
				// probably to guarantee it paints on top. AnimateWindow has another side effect
				// that it causes a PerformLayout, which is why isAnimating is set to true (above).
				int x = Controls.IndexOf(c2);
				AnimateWindow(c2, AnimateOpenMillis, AnimateOpenEffect);
				Controls.SetChildIndex(c2, x); // set index back
				c2.Visible = true; // oddly, c2's Visible is still false after the animation.
				if (holdSpace)
					cb.Margin = mOrig; // put back original margin

				if (resizeBar != null && ResizeBarsFadeProximity == 0)
					resizeBar.Visible = true;

				isAnimating = false;
			}
			else if (!b && AnimateCloseEffect != AnimateWindowFlags.None && AnimateCloseMillis > 0) {
				isAnimating = true; // prevent c2.Visible from triggering PerformLayout
				// close animation is much simpler than open animation
				// Note: closing doesn't swap the index of c2.
				AnimateWindow(c2, AnimateCloseMillis, AnimateCloseEffect);
				// very important: must set the sizes to zero _before_ hiding the control,
				// otherwise scrollbar artifacts will appear. To reproduce issue, use Test4 tab,
				// open Parent3, use the Fill Down button twice. Scroll the accordion a little,
				// then close Parent3. The vertical scrollbar is left on the screen.
				c2.c.Size = Size.Empty;
				c2.Size = Size.Empty;
				c2.Visible = false;
				isAnimating = false;
				InternalPerformLayout(); // must come after animation
			}
			else {
				isAnimating = true;
				c2.Visible = b;
				isAnimating = false;
				layout(false);
			}

			if (b) {
				c2.c.Focus();
				if (!c2.c.CanSelect)
					c.SelectNextControl(c, true, true, true, true);
			}
		};

		cb.VisibleChanged += delegate {
			bool b = cb.Visible && cb.Checked;
			if (c2.Visible != b) {
				isAdjusting = true;
				c2.Visible = b;
				if (c2.ResizeBar != null && ResizeBarsFadeProximity == 0) {
					c2.ResizeBar.Visible = b;
				}
				isAdjusting = false;
				InternalPerformLayout();
			}
		};

		layout(true);
		return cb;
	}

	protected override void WndProc(ref Message m) {
		if (ignoreNCCALCSIZE && m.Msg == WM_NCCALCSIZE || ignoreNCPAINT && (m.Msg == WM_NCPAINT || m.Msg == WM_ERASEBKGND)) {
			return;
		}
		base.WndProc(ref m);
	}

	private Accordion InternalPerformLayout() {
		// have to call it at least twice to force scrollbars to refresh
		// I think it's a timing issue, and the queuing up a bunch of calls
		// means the actual execution is delayed. Since it waits longer, the
		// end result is more accurate.
		PerformLayout();
		Control p = Parent;
		Accordion tma = this;
		while (p != null) {
			if (p is Accordion) {
				p.PerformLayout();
				tma = (Accordion) p;
			}
			p = p.Parent;
		}

		PerformLayout();
		tma.PerformLayout();
		return tma;
	}

	///<summary>Returns the number of controls that are added to this Accordion.</summary>
	public int Count {
		get {
			return Control2s.Count;
		}
	}

	///<summary>Returns the n'th CheckBox header.</summary>
	public CheckBox CheckBox(int i) {
		return Control2s[i].cb;
	}

	///<summary>Returns the n'th Control.</summary>
	public Control Content(int i) {
		return Control2s[i].c;
	}

	///<summary>Returns the resize bar of the n'th Control, or null if that control does not have a resize bar.</summary>
	public Control ResizeBar(int i) {
		return Control2s[i].ResizeBar;
	}

	///<summary>Returns an enumerator of all non-null resize bars in this Accordion.</summary>
	public IEnumerable<Control> ResizeBars {
		get {
			foreach (Control c in ResizeBarsList)
				yield return c;
		}
	}

	///<summary>Finds the header CheckBox for the specified control. This can be useful
	///when using an ErrorProvider and you want to display an error icon beside both the control
	///and beside the header checkbox (especially if the header checkbox is closed).</summary>
	///<param name="c">Any control or child of a control that was added to this accordion.</param>
	///<returns>Returns the checkbox if the control is found, otherwise null is returned.</returns>
	public CheckBox CheckBoxForControl(Control c) {
		c = c.Parent;
		while (c != null) {
			if (c is Control2 && c.Parent == this)
				return ((Control2) c).cb;

			c = c.Parent;
		}
		return null;

		//Accordion2 acc = this;
		//for (int i = 0; i < acc.Count; i++) {
		//	CheckBox cb = acc.CheckBox(i);
		//	Control parent = acc.Content(i);
		//	if (Contains(parent, c))
		//		return cb;
		//}
		//return null;
	}

	//private static bool Contains(Control parent, Control c) {
	//	if (parent == c)
	//		return true;
	//	foreach (Control c2 in parent.Controls) {
	//		bool b = Contains(c2, c);
	//		if (b)
	//			return b;
	//	}
	//	return false;
	//}

	private static Padding Get(params Padding?[] arr) {
		foreach (Padding? p in arr)
			if (p.HasValue)
				return p.Value;
		return Padding.Empty;
	}

	private String GetDownArrow() {
		return (this.DownArrow == null ? GlobalDownArrow : this.DownArrow);
	}

	private String GetUpArrow() {
		return (this.UpArrow == null ? GlobalUpArrow : this.UpArrow);
	}

	///<summary>Closes the specified controls. If a control cannot be found then it is skipped.</summary>
	public void Close(params Control[] controls) {
		Open(controls, false);
	}

	///<summary>Opens the specified controls. If a control cannot be found then it is skipped.</summary>
	public void Open(params Control[] controls) {
		Open(controls, true);
	}

	private void Open(Control[] controls, bool open) {
		isAdjusting = true;
		bool changed = false;
		Control2 last = null;
		foreach (Control2 c2 in Control2s) {
			Control2 c = null;
			if (controls == null)
				c = c2;
			else {
				foreach (Control cc in controls) {
					if (cc == c2.c) {
						c = c2;
						break;
					}
				}
			}
			if (c != null) {
				last = c;
				if (c.cb.Checked != open) {
					changed = true;
					c.cb.Checked = open;
				}
			}
		}
		isAdjusting = false;

		if (changed) {
			//UpdateDeltaHeights();
			InternalPerformLayout();
		}
	}

	private static AnchorStyles Map(DockStyle d) {
		if (d == DockStyle.Bottom)
			return AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Bottom;
		if (d == DockStyle.Fill)
			return AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
		if (d == DockStyle.Left)
			return AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left;
		if (d == DockStyle.Right)
			return AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Right;
		if (d == DockStyle.Top)
			return AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top;
		return AnchorStyles.None;
	}


	///<summary>Handles the mouse resize events for increasing or decreasing the height of controls.</summary>
	public bool PreFilterMessage(ref Message m) {
		if (!Enabled)
			return false;

		if (m.Msg == WM_KEYDOWN) {
			int key = m.WParam.ToInt32();
			if (ResizeBarsArrowKeyDelta != 0 && (key == VK_UP || key == VK_DOWN) && currentControl2 != null) {
				var c2 = currentControl2;
				int newDh = c2.dh;
				if (key == VK_UP)
					newDh = Math.Max(c2.dh - ResizeBarsArrowKeyDelta, c2.MinDH);
				else if (key == VK_DOWN)
					newDh = Math.Min(c2.dh + ResizeBarsArrowKeyDelta, c2.MaxDH);

				if (c2.dh != newDh) {
					c2.isLocked = true;
					c2.dh = newDh;
					isOpening = ResizeBarsStayInViewOnArrowKey;
					isDragging = true; // set is dragging or resize bar is hidden if partially visible
					InternalPerformLayout();
					isDragging = false;
					isOpening = false;
				}
				return true;
			}
		}
		else if (m.Msg == WM_MOUSEMOVE) {
			// LParam is relative to the control the mouse is above
			// Point pt = new Point(m.LParam.ToInt32());
			// instead we need the absolute location:
			Point pt = Cursor.Position;

			if (isDragging) {
				if (oldPoint == pt || !AllowMouseResize) {
					// same points are fired when dragging, so just return
					return false;
				}
				int newdh = originalDH + (pt.Y - grabPoint.Y);
				int minDH = grabControl.MinDH;
				if (newdh < minDH)
					newdh = minDH;

				int maxDH = grabControl.MaxDH;
				if (newdh > maxDH)
					newdh = maxDH;

				if (newdh == grabControl.dh)
					return false;

				wasDragged = true;
				grabControl.dh = newdh;
				resetLocked = false;
				PerformLayout();
				oldPoint = pt;
				return false;
			}
			else if (ResizeBarsFadeProximity > 0) {
				//Point pt = new Point(m.LParam.ToInt32());
				Point pt2 = PointToClient(pt); // relative to this Accordion
				FadeResizeBars(pt2, pt);
			}

			// determine if the cursor is in the bounds of the Accoridion
			var bounds = new Rectangle(PointToScreen(Point.Empty), Size);

			if (!bounds.Contains(pt))
				return false;

			Control2 c2 = FindControl2(pt);

			if (c2 != null) {
				Cursor = GrabCursor;
			}
			else {
				// only reset cursor if it needs it, otherwise if the
				// mouse is over a textbox (for example), the cursor
				// will be the pointer and not the IBeam.
				if (Cursor == GrabCursor)
					Cursor = DefaultCursor;
			}
		}
		else if (m.Msg == WM_LBUTTONDOWN) {
			wasDragged = false;
			Point pt = Cursor.Position;
			Control2 c2 = FindControl2(pt);

			if (c2 != null) {
				var c3 = ControlAtPoint(pt);
				if (c3 is ScrollBar) {
					// if a grabbable area overlaps a scroll bar, then a
					// mouse down on a ScrollBar makes it consume the mouse events
					// so we need to release it. Are there other controls that also
					// need to be released?
					c3.BeginInvoke((Action) delegate {
						ReleaseCapture();
					});
				}

				// is hwnd a child of c2?
				hwndPreviousFocus = GetFocus();
				var h = hwndPreviousFocus;
				while (h != IntPtr.Zero) {
					h = GetParent(h);
					if (h == c2.Handle)
						break;
				}
				if (h == IntPtr.Zero)
					hwndPreviousFocus = h;

				if (c2.ResizeBar != null)
					c2.ResizeBar.Focus();

				grabControl = c2; 
				origLocked = c2.isLocked;
				c2.isLocked = true;
				isDragging = true;
				resetLocked = true;
				originalDH = c2.dh;
				grabPoint = pt;
				// don't return true here, otherwise if the mouse
				// is dragged off the window then no more mouse move
				// events are received.
				//return true;
			}
			else {
				isDragging = false;
			}
		}
		else if (m.Msg == WM_LBUTTONUP) {
			Control2 c2 = grabControl;
			grabControl = null;
			isDragging = false; // set to false before restoring the focus, otherwise the scrollbar jumps

			if (c2 != null) {
				if (resetLocked)
					c2.isLocked = origLocked;

				if (c2.ResizeBar != null && c2.ResizeBar.Visible) {
					if (wasDragged) {
						if (!ResizeBarsKeepFocusAfterMouseDrag)
							RestoreFocus(c2.c);
					}
					else {
						// no drag happened
						if (!ResizeBarsKeepFocusOnClick)
							RestoreFocus(c2.c);
					}
				}
			}
		}
		return false;
	}

	// pt needs to be in screen coordinates
	private Control2 FindControl2(Point pt) {
		// the mouse should only turn into a grab cursor if the accordion is in the window that
		// is currently the foreground window, AND the mouse is directly over _this_ accordion (or
		// one of the accordion's child controls)
		var th = GetTopMostHandle(this.Handle); // works for both WPF (e.g. WindowsFormsHost) and Winforms
		var fg = GetForegroundWindow();

		// Note: bounds is not accurate because using a TabControl, different accordions can occupy the
		// same region.
		//var bounds = new Rectangle(PointToScreen(Point.Empty), Size);
		if (fg != th || !IsMouseOverThisControl(pt))
			return null;

		int gw = GrabWidth;
		Control2 c = null;

		foreach (Control2 c2 in Control2s) {
			if (!c2.Visible)
				continue;

			//c2.BackColor = Color.Transparent; // testing only
			//if (b2.Contains(pt))
			//	c2.BackColor = Color.Yellow;

			int y = 0;
			int dy = 0;
			bool canGrab = false;
			if (c2.ResizeBar != null) {
				if (c2.ResizeBar.Visible) {
					canGrab = true;
					var b3 = new Rectangle(c2.ResizeBar.PointToScreen(Point.Empty), c2.ResizeBar.Size);
					//c2.BackColor = Color.Transparent; // testing only
					if (b3.Contains(pt)) {
						dy = 1;
						//c2.BackColor = Color.Yellow;
					}
				}
			}
			else {
				var b2 = new Rectangle(c2.PointToScreen(Point.Empty), c2.Size);
				y = b2.Y + b2.Height;
				dy = y - pt.Y;
				// only grab when in the range
				canGrab = !GrabRequiresPositiveFillWeight || GrabRequiresPositiveFillWeight && c2.fillWt > 0;
			}

			if (dy > 0 && dy <= gw && canGrab) {
				c = c2;
				break;
			}
		}
		return c;
	}

	private void RestoreFocus(Control c) {
		// re: ResizeBarsKeepFocusIfControlOutOfView
		// originally this was done to prevent the scrollbar from jumping, but
		// overriding the ScrollToControl fixed that problem.

		if (hwndPreviousFocus != IntPtr.Zero) {
			if (!ResizeBarsKeepFocusIfControlOutOfView)
				SetFocus(hwndPreviousFocus);
			else {
				Rectangle accBounds = new Rectangle(PointToScreen(Point.Empty), Size);
				RECT r = new RECT();
				GetWindowRect(hwndPreviousFocus, out r);
				if (IsOverlapping(accBounds, r))
					SetFocus(hwndPreviousFocus);
			}
		}
		else {
			if (!ResizeBarsKeepFocusIfControlOutOfView) {
				c.Focus();
				if (!c.CanSelect)
					c.SelectNextControl(c, true, true, true, true);
			}
			else {
				Rectangle accBounds = new Rectangle(PointToScreen(Point.Empty), Size);
				// c.CanSelect is false when c is some type of container control that hosts other controls.
				// otherwise it's not clear to the user which control has the focus.
				if (!c.CanSelect)
					c = c.GetNextControl(c, true);

				if (c != null) {
					RECT r = new RECT();
					GetWindowRect(c.Handle, out r);
					if (IsOverlapping(accBounds, r))
						c.Focus();
				}
			}
		}
	}

	private static bool IsOverlapping(Rectangle r0, RECT r) {
		return (r.Top >= r0.Top && r.Top <= r0.Bottom ||
				r.Bottom >= r0.Top && r.Bottom <= r0.Bottom ||
				r.Top <= r0.Top && r.Bottom >= r0.Bottom);
	}

	protected override void OnMouseLeave(EventArgs e) {
		base.OnMouseLeave(e);
		if (ResizeBarsFadeProximity > 0) {
			Point pt = Cursor.Position;
			Rectangle r = new Rectangle(PointToScreen(Point.Empty), Size);
			if (!r.Contains(pt)) {
				if (ResizeBarsFadeProximity > 0) {
					resizeBarHiding = null;
					foreach (Control rb in ResizeBarsList) {
						if (rb.Focused) {
							if (ResizeBarsStayVisibleIfFocused)
								continue;
							else
								resizeBarHiding = rb;
						}

						rb.FadeOut(ResizeBarsFadeOutMillis);
					}
				}
			}
		}
	}

	private void FadeResizeBars(Point pt, Point absPt) {
		bool isOverCheckBox = false;
		IntPtr hWnd = WindowFromPoint(absPt);
		foreach (Control2 c2 in Control2s) {
			var cb = c2.cb;
			if (cb.Visible) {
				if (hWnd == cb.Handle) {
					isOverCheckBox = true;
					break;
				}
			}
		}

		resizeBarHiding = null;
		foreach (Control c in Controls) {
			if (!(c is Control2))
				continue;

			Control2 c2 = (Control2) c;
			if (!c2.cb.Checked || c2.ResizeBar == null)
				continue;

			var rb = c2.ResizeBar;
			var r = rb.Bounds;
			int distance = Distance(r, pt);
			bool isNear = (distance <= ResizeBarsFadeProximity);

			// don't fade-in if over a checkbox
			if (isNear && !isOverCheckBox) {
				// could do this, but it's nicer to always fade.
				//if (!c2.ResizeBarIsPartiallyVisible || ShowPartiallyVisibleResizeBars)
				rb.FadeIn(ResizeBarsFadeInMillis);
			}
			else {
				// don't hide the resize bar if it has the focus.
				// the user may want to use th up/down keys to resize it more
				bool b = rb.Focused;
				if (!b || b && !ResizeBarsStayVisibleIfFocused) {
					if (b)
						resizeBarHiding = rb;

					rb.FadeOut(ResizeBarsFadeOutMillis);
				}
			}
		}
	}

	private static int Distance(Rectangle r, Point p) {
		var dx = Math.Max(r.X - p.X, p.X - (r.X + r.Width));
		if (dx < 0)
			dx = 0;
		var dy = Math.Max(r.Y - p.Y, p.Y - (r.Y + r.Height));
		if (dy < 0)
			dy = 0;
		return (int) Math.Sqrt(dx * dx + dy * dy);
	}

	private class Control2 : UserControl {
		internal Control c;
		internal CheckBox cb;
		internal double fillWt = 0;
		internal int dh = 0;
		internal DateTime lastClicked = DateTime.MinValue;
		internal bool isLocked = false;
		//--
		internal LayoutArgs layoutArgs;
		internal Control ResizeBar { get; set; }
		internal bool ResizeBarIsPartiallyVisible = false;
		internal Padding resizeBarMargin = Padding.Empty;

		public Control2(CheckBox cb, Control c, Control resizeBar, double fillWt, LayoutArgs layoutArgs) {
			this.cb = cb;
			this.c = c;
			this.fillWt = fillWt;
			this.layoutArgs = layoutArgs;
			Visible = cb.Checked;
			Controls.Add(c);
			ResizeBar = resizeBar;
			//-----
			AutoSize = true;
			Margin = Padding.Empty;
			//TabStop = false; // DO NOT SET FALSE. Otherwise controls in this control cannot be tabbed into.
			//-----
			AutoSizeMode = AutoSizeMode.GrowAndShrink;
			BorderStyle = BorderStyle.None;
			//AutoScroll = false; // determine if true/false or user defined should be used
			if (resizeBar != null) {
				// Resize bars should not assign a margin because it will trigger the scrollbars to appear.
				// During testing, left and right margins of 100 were used, which would cause the scrollbars
				// to flash at certain widths. Instead, the margin is cached.
				resizeBarMargin = resizeBar.Margin;
				resizeBar.Margin = Padding.Empty;
				bool flag = false;
				resizeBar.MarginChanged += delegate {
					if (flag)
						return;
					resizeBarMargin = resizeBar.Margin;
					flag = true;
					resizeBar.Margin = Padding.Empty;
					flag = false;
				};
			}
		}

		public override Size MinimumSize {
			get {
				Size s = c.MinimumSize;
				Padding p = this.Padding;
				Padding m = c.Margin;
				s.Width += p.Horizontal + m.Horizontal;
				s.Height += p.Vertical + m.Vertical;
				return s;
			}
			set {
				base.MinimumSize = value;
			}
		}

		// a negative value [-x, 0]
		public int MinDH {
			get {
				Accordion a = (Accordion) Parent;
				if (a.ControlMinimumHeightIsItsPreferredHeight)
					return 0;

				Size min = c.MinimumSize;
				Size ps = c.PreferredSize;
				return Math.Min(min.Height - ps.Height, 0);
			}
		}

		// a positive value [0, x]
		public int MaxDH {
			get {
				Size max = c.MaximumSize;
				if (max.Height == 0)
					return int.MaxValue;

				Size ps = c.PreferredSize;
				int maxDH = max.Height - ps.Height;
				return Math.Max(maxDH, 0);
			}
		}

		public override Size MaximumSize {
			get {
				Size s = c.MaximumSize;
				Padding p = this.Padding;
				Padding m = c.Margin;
				if (s.Height > 0)
					s.Height += (p.Vertical + m.Vertical);

				if (s.Width > 0)
					s.Width += (p.Horizontal + m.Horizontal);

				return s;
			}
			set {
				base.MaximumSize = value;
			}
		}

		public override Size GetPreferredSize(Size proposedSize) {
			Size s = GetPreferredSize(proposedSize, true, true);
			return s;
		}

		internal Size GetPackSize() {
			return GetPreferredSize(Size.Empty, false, false);
		}

		internal Size GetPreferredSize(Size proposedSize, bool addDH, bool returnEmptyIfClosed) {
			if (returnEmptyIfClosed && !cb.Checked)
				return Size.Empty;

			// cannot use base.GetPreferredSize(...)
			// UserControl has no defined layout, so it makes sense
			// that the returned size doesn't look at the children
			Size s = c.GetPreferredSize(proposedSize);
			Padding p = this.Padding;
			Padding m = c.Margin;
			s.Width += p.Horizontal + m.Horizontal;
			s.Height += p.Vertical + m.Vertical;

			if (addDH)
				s.Height += dh;

			return s;
		}
	}

	internal bool IsResizeBar(Control c) {
		if (c == null)
			return false;
		return ResizeBarsList.Contains(c);
	}

	public override Size GetPreferredSize(Size proposedSize) {
		bool includeInvisible = !this.Visible;
		return layoutEngine.GetPreferredSize(this, true, true, includeInvisible);
	}

	public override LayoutEngine LayoutEngine {
		get {
			return layoutEngine;
		}
	}

	// OnScroll is not triggered by mouse wheel, so it must be handled too.
	protected override void OnMouseWheel(MouseEventArgs e) {
		base.OnMouseWheel(e);
		if (VerticalScroll.Visible)
			UpdateResizeBarsPartiallyVisibleFlag();
	}

	protected override void OnScroll(ScrollEventArgs se) {
		base.OnScroll(se);

		if (se.ScrollOrientation == ScrollOrientation.VerticalScroll) {
			UpdateResizeBarsPartiallyVisibleFlag();
		}
	}

	private void UpdateResizeBarsPartiallyVisibleFlag() {
		// as the accordion is vertically scrolled, resize bars that are outside of the
		// viewable area should no longer be accessible, and those that come into the viewable area are
		// now available.
		var s = ClientSize; // use ClientSize since it accounts for currently visible scrollbars
		Point ptTopLeft = PointToScreen(Point.Empty);
		Point ptBottomRight = PointToScreen(new Point(s.Width, s.Height));

		bool needsRefresh = false;
		foreach (Control c in Controls) {
			if (!c.Visible || !(c is Control2))
				continue;

			Control2 c2 = (Control2) c;
			if (c2.ResizeBar == null)
				continue;

			var r2 = c2.ResizeBar.Bounds;
			Point ptTopLeft2 = PointToScreen(r2.Location);
			Point ptBottomRight2 = PointToScreen(new Point(r2.X + r2.Width, r2.Y + r2.Height));

			bool isPartiallyVisible = ptTopLeft2.Y < ptTopLeft.Y || ptBottomRight2.Y > ptBottomRight.Y;
			c2.ResizeBarIsPartiallyVisible = isPartiallyVisible;

			if (ResizeBarsFadeProximity == 0) {
				bool show =	ShowPartiallyVisibleResizeBars || !isPartiallyVisible || c2.ResizeBar.Focused && ResizeBarsStayVisibleIfFocused;
				if (c2.ResizeBar.Visible != show) {
					needsRefresh = true;
					c2.ResizeBar.Visible = show;
				}
			}
		}

		if (needsRefresh)
			Refresh();
	}

	internal class AccordionLayoutEngine : LayoutEngine {

		//public override void InitLayout(Object child, BoundsSpecified specified) {}
		int maxPreferredWidth = 0;
		int maxPreferredHeight = 0;

		public override bool Layout(Object container, LayoutEventArgs layoutEventArgs) {
			Accordion acc = (Accordion) container;
			if (acc.isAdjusting)
				return false;

			if (acc.isAnimating || acc.IsResizeBar(layoutEventArgs.AffectedControl))
				return false;

			Size clientSize = acc.ClientSize; // ClientSize accounts for currently visible scrollbars
			Size avail = clientSize;

			Size prefNoDH = GetPreferredSize(acc, false, true, false); // accounts for padding
			UpdateDeltaHeights(acc, avail.Height, prefNoDH.Height);

			Size pref = GetPreferredSize(acc, true, true, false); // calculate pref after DHs are updated
			if (acc.FillWidth) {
				if (avail.Width >= pref.Width) {} // do nothing
				else {
					// if GrowAndShrink is false, or control's must be at least as wide as their preferred
					// size, then set the available width to be the preferred width.
					if (!acc.GrowAndShrink || acc.ControlMinimumWidthIsItsPreferredWidth)
						avail.Width = pref.Width;
				}
			}
			else {
				if (acc.GrowAndShrink) {
					maxPreferredWidth = 0;
					avail.Width = pref.Width;
				}
				else {
					if (pref.Width > maxPreferredWidth)
						maxPreferredWidth = pref.Width;
					avail.Width = maxPreferredWidth;
				}
			}

			if (!acc.FillHeight) {
				if (acc.GrowAndShrink) {
					maxPreferredHeight = 0;
					if (avail.Height > prefNoDH.Height) {
						avail.Height = prefNoDH.Height;
						UpdateDeltaHeights(acc, avail.Height, prefNoDH.Height);
					}
				}
				else {
					if (prefNoDH.Height > maxPreferredHeight)
						maxPreferredHeight = prefNoDH.Height;

					avail.Height = maxPreferredHeight;
					UpdateDeltaHeights(acc, avail.Height, prefNoDH.Height);
				}
			}

			Padding p = acc.Padding;
			avail.Height -= p.Vertical;
			avail.Width -= p.Horizontal;

			bool vScrollBarVisible = acc.VerticalScroll.Visible;
			bool hScrollBarVisible = acc.HorizontalScroll.Visible;
			int offsetX = 0;
			int offsetY = 0;
			if (hScrollBarVisible)
				offsetX = -acc.HorizontalScroll.Value;

			if (vScrollBarVisible)
				offsetY = -acc.VerticalScroll.Value;

			// when performing an actual layout, the bottom padding is never added to the size because the padding does not require scrollbars
			Size calcSize = LayoutInternal(false, acc, offsetX, offsetY, avail, p, false, clientSize, true, true, false);

			// The key to having non-flickering scrollbars is to determine if the scrollbar is about to be shown.
			// A scrollbar will be shown if a control is outside of the viewable client area. If a scrollbar isn't currently
			// visible, then account for the horizontal and vertical spaces the scrollbars will occupy.
			// If the client size and preferred size are equal, then there are no scrollbars. If the control cannot shrink
			// but the client size is made smaller, then scrollbars appear. If controls incorrectly allocate extra width, then it's
			// possible the scrollbars will appear if the client size is made larger.
			int dww = 0;
			if (calcSize.Height > clientSize.Height) {
				if (!vScrollBarVisible && acc.AutoScroll) {
					int dw = SystemInformation.VerticalScrollBarWidth;
					avail.Width -= dw;

					// Since the width is decreased, it means there is going to be a vertical scrollbar. The original calcSize.Width was done
					// with the ClientSize that did not subtract the VerticalScrollBarWidth (because vScrollBarVisible is false).
					// Note: cannot simply subtract dw from clientSize.Width because there may be minimum size constraints.
					Size calcSize2 = LayoutInternal(false, acc, offsetX, offsetY, avail, p, false, clientSize, true, true, false);
					calcSize = calcSize2;
					dww = dw;
				}
			}

			if (calcSize.Width > clientSize.Width - dww) {
				if (!hScrollBarVisible && acc.AutoScroll) {
					int dh = SystemInformation.HorizontalScrollBarHeight;
					avail.Height -= dh;
					// since height is removed, the DHs need to be recalculated
					//UpdateDeltaHeights(acc, clientSize.Height - dh, prefNoDH.Height);
					UpdateDeltaHeights(acc, avail.Height + p.Vertical, prefNoDH.Height);
				}
			}

			LayoutInternal(true, acc, offsetX, offsetY, avail, p, false, clientSize, true, true, false);

			return false;
		}

		// returns the calculated size needed to display the controls
		private Size LayoutInternal(bool doLayout, Accordion acc, int offsetX, int offsetY, Size avail, Padding p, bool calcPreferredSize, Size clientSize, bool addDH, bool returnEmptyIfClosed, bool includeInvisible) {
			Control lastResizeBar = null;
			Point ptTopLeft = Point.Empty;
			Point ptBottomRight = Point.Empty;
			if (doLayout) {
				ptTopLeft = acc.PointToScreen(Point.Empty);
				ptBottomRight = acc.PointToScreen(new Point(clientSize.Width, clientSize.Height));
				foreach (Control2 c2 in acc.Control2s) {
					if (c2.Visible)
						lastResizeBar = c2.ResizeBar;
					else if (c2.cb.Visible)
						lastResizeBar = null;
				}
			}

			Size s = Size.Empty;
			bool isRightToLeft = (acc.RightToLeft == RightToLeft.Yes);
			int px = p.Left;
			int py = p.Top;

			ControlCollection controls = acc.Controls;
			int n = controls.Count;

			for (int i = 0; i < n; i++) {
				Control c = controls[i];
				if (acc.IsResizeBar(c)) // || !c.Visible (don't skip invisible here)
					continue;

				Size ps = Size.Empty;
				if (c is Control2) {
					Control2 c2 = (Control2) c;
					if (includeInvisible || c2.cb.Visible) {
						if (returnEmptyIfClosed && !c2.cb.Checked)
							continue;

						ps = c2.GetPreferredSize(Size.Empty, addDH, returnEmptyIfClosed);
					}
					else {
						// control2s with an invisible checkbox do not add to the preferred height
						continue;
					}
				}
				else {
					if (includeInvisible || c.Visible)
						ps = c.GetPreferredSize(Size.Empty);
					else {
						// invisible checkboxes do not add to the preferred height
						continue;
					}
				}

				Padding cm = c.Margin;
				int x = px + cm.Left + offsetX;
				int y = py + cm.Top + offsetY;
				int w = 0;
				int h = 0;

				bool isMin = false;

				if (calcPreferredSize) {
					w = ps.Width;
					h = ps.Height;
				}
				else {
					int minH = ps.Height;
					int minW = ps.Width;
					bool isMin2 = false;
					if (!acc.ControlMinimumHeightIsItsPreferredHeight || !acc.ControlMinimumWidthIsItsPreferredWidth) {
						Size min = c.MinimumSize;
						if (!acc.ControlMinimumHeightIsItsPreferredHeight)
							minH = min.Height;
						if (!acc.ControlMinimumWidthIsItsPreferredWidth) {
							minW = min.Width;
							isMin2 = true;
						}
					}

					Size max = c.MaximumSize;
					w = avail.Width - (cm.Horizontal);
					h = ps.Height;

					if (w < minW) {
						w = minW;
						isMin = isMin2;
					}
					if (h < minH)
						h = minH;

					if (max.Height > 0 && h > max.Height)
						h = max.Height;

					if (max.Width > 0 && w > max.Width)
						w = max.Width;
				}

				py += (h + cm.Vertical);

				int right = px + offsetX + cm.Horizontal + w;
				if (right > s.Width)
					s.Width = right;

				if (doLayout) {
					if (!c.Visible) {
						continue;
					}

					c.SetBounds(x, y, w, h);

					if (c is Control2) {
						Control2 c2 = (Control2) c;
						Control d = c2.c;

						if (c2.ResizeBar != null) {
							var rb = c2.ResizeBar;
							Padding rm = c2.resizeBarMargin;
							int rx = 0;
							int rw = (int) ((avail.Width - rm.Horizontal) * acc.ResizeBarsFill);
							if (isMin && rw < w) {
								// if the minimum size width is met, then align the resize bar to the
								// control exactly (looks nicer)
								rw = w;
								rx = x;
							}
							else {
								if (rw < acc.ResizeBarsMinimumLength) {
									// must take avail.Width if smaller, otherwise scrollbars oscillate on and off
									rw = Math.Min(acc.ResizeBarsMinimumLength, avail.Width);
								}

								var cbBounds = c2.cb.Bounds;
								int r1 = x + w;
								int r2 = cbBounds.Right;
								int maxR = Math.Max(r1, r2);
								int align = Math.Max(0, (int) ((avail.Width - (rm.Horizontal + rw)) * acc.ResizeBarsAlign));

								rx = (px + rm.Left + offsetX + align);
								if (rx + rw > maxR - rm.Left)
									rx = x + Math.Max(0, (maxR - (x + rw)) / 2);
							}

							int rh = rb.Height;
							int ry = (y + h) - (rh/2) + rm.Top;

							if (c2.ResizeBar == lastResizeBar) {
								// if there is an insufficient margin, then the 
								// resize bar is moved up so that it does not exceed the margin.
								if (ry + rh > y + h + cm.Bottom)
									ry = y + h + cm.Bottom - rh;
							}

							Point ptTopLeft2 = acc.PointToScreen(new Point(rx, ry));
							Point ptBottomRight2 = acc.PointToScreen(new Point(rx + rw, ry + rh));

							bool isPartiallyVisible = ptTopLeft2.Y < ptTopLeft.Y || ptBottomRight2.Y > ptBottomRight.Y;
							c2.ResizeBarIsPartiallyVisible = isPartiallyVisible;

							if (acc.ResizeBarsFadeProximity == 0) {
								// hide the resize bar if it is partially visible and partially visible resize bars are hidden,
								// but don't hide it if it has the focus or is being resized.
								bool b = acc.ShowPartiallyVisibleResizeBars || !isPartiallyVisible || (rb.Focused && (acc.ResizeBarsStayVisibleIfFocused || acc.isDragging));
								rb.Visible = b; // || acc.isDragging; <-- this would keep all resize bars visible during a drag
							}

							rb.SetBounds(rx, ry, rw, rh);
						}

						if (d.Dock == DockStyle.None) {
							double alignX = 0;
							double alignY = 0;
							double fillX = 0;
							double fillY = 0;
							if (d.Anchor == AnchorStyles.None) {
								if (c2.layoutArgs != null) {
									var la = c2.layoutArgs;
									alignX = la.AlignX;
									alignY = la.AlignY;
									fillX = la.FillX;
									fillY = la.FillY;
								}
							}
							else {
								var a = d.Anchor;
								if (a == AnchorStyles.Bottom) {
									alignX = 0.5;
									alignY = 1.0;
								}
								else if (a == AnchorStyles.Top) {
									alignX = 0.5;
									alignY = 0.0;
								}
								else if (a == AnchorStyles.Left) {
									alignX = 0.0;
									alignY = 0.5;
								}
								else if (a == AnchorStyles.Right) {
									alignX = 1.0;
									alignY = 0.5;
								}
								else if (a == (AnchorStyles.Left | AnchorStyles.Right)) {
									alignX = 0.0;
									alignY = 0.5;
									fillX = 1.0;
								}
								else if (a == (AnchorStyles.Left | AnchorStyles.Top)) {
									alignX = 0.0;
									alignY = 0.0;
								}
								else if (a == (AnchorStyles.Left | AnchorStyles.Bottom)) {
									alignX = 0.0;
									alignY = 1.0;
								}
								else if (a == (AnchorStyles.Right | AnchorStyles.Top)) {
									alignX = 1.0;
									alignY = 0.0;
								}
								else if (a == (AnchorStyles.Right | AnchorStyles.Bottom)) {
									alignX = 1.0;
									alignY = 1.0;
								}
								else if (a == (AnchorStyles.Top | AnchorStyles.Bottom)) {
									alignX = 0.5;
									alignY = 0.0;
									fillY = 1.0;
								}
								else {
									alignX = 0;
									alignY = 0;
									fillX = 1;
									fillY = 1;
								}
							}

							if (isRightToLeft)
								alignX = 1.0 - alignX;

							Padding c2p = c2.Padding;
							Padding dm = d.Margin;

							int availH1 = Math.Max(0, h - (dm.Vertical + c2p.Vertical));
							int availW1 = Math.Max(0, w - (dm.Horizontal + c2p.Horizontal));

							// the size of the control cannot exceed the available width and height
							Size ds = d.PreferredSize;
							ds.Height = Math.Min(availH1, ds.Height);
							ds.Width = Math.Min(availW1, ds.Width);

							int extraW1 = Math.Max(0, availW1 - ds.Width);
							int extraH1 = Math.Max(0, availH1 - ds.Height);

							int w1 = ds.Width + (int) (fillX * extraW1);
							int h1 = ds.Height + (int) (fillY * extraH1);
							Size dMax = d.MaximumSize;
							if (dMax.Width > 0 && w1 > dMax.Width)
								w1 = dMax.Width;
							if (dMax.Height > 0 && h1 > dMax.Height)
								h1 = dMax.Height;

							int freeh = (w - (w1 + dm.Horizontal + c2p.Horizontal));
							int freev = (h - (h1 + dm.Vertical + c2p.Vertical));

							int x1 = dm.Left + c2p.Left + (int) (alignX * freeh);
							int y1 = dm.Top + c2p.Top + (int) (alignY * freev);

							d.SetBounds(x1, y1, w1, h1);
						}
					}
				}
			}

			s.Height = py;

			// For the preferred size calculation, the bottom and right padding are added
			// They are not added for the other calculation because the padding does not
			// activate the scrollbars.
			if (calcPreferredSize) {
				s.Width += p.Right;
				s.Height += p.Bottom;
			}

			return s;
		}

		public Size GetPreferredSize(Accordion a, bool addDH, bool returnEmptyIfClosed, bool includeInvisible) {
			Size s = LayoutInternal(false, a, 0, 0, Size.Empty, a.Padding, true, Size.Empty, addDH, returnEmptyIfClosed, includeInvisible);
			return s;
		}

		private void UpdateDeltaHeights(Accordion acc, int clientSizeHeight, int prefHeightNoDH) {
			bool fillLastOpened = acc.FillLastOpened;
			bool fillModeGrowOnly = acc.FillModeGrowOnly;

			double totalWt = 0;
			int mh = 0; // minus height
			Control2 fillControl = null;
			foreach (Control2 c2 in acc.Control2s) {
				if (c2.cb.Checked) {
					if (c2.isLocked) {
						// it's OK if dh is negative, it means a control is smaller than its preferred height,
						// which means more space is available for other controls
						mh += c2.dh;
					}
					else {
						// reset dh to zero because the available space may flip, leaving the old large value
						if (!acc.FillModeGrowOnly)
							c2.dh = 0;

						totalWt += c2.fillWt;

						if (c2.fillWt > 0 && (fillControl == null || c2.lastClicked > fillControl.lastClicked))
							fillControl = c2;
					}
				}
			}

			int eh = (clientSizeHeight - prefHeightNoDH) - mh;

			if (fillLastOpened) {
				if (fillControl != null) {
					if (eh > 0)
						eh = Math.Min(eh, fillControl.MaxDH);
					else
						eh = Math.Max(eh, fillControl.MinDH);

					if (fillModeGrowOnly) {
						if (eh > fillControl.dh)
							fillControl.dh = eh;
					}
					else {
						fillControl.dh = eh;
					}
				}
				else {
				}
			}
			else {
				if (eh < 0 && totalWt > 0) {
					// If there is not enough space, then controls that have a MinDH < 0 can
					// be smaller than their preferred height. Controls decrease at a rate
					// proportional to their fillWt with respect to other controls with a
					// positive fillWt that are currently not locked.
					bool[] isLocked = new bool[acc.Control2s.Count];
					int[] minDHs = new int[acc.Control2s.Count];
					int mh2 = 0;
					bool first = true;
					do {
						mh2 = 0;
						double pixels2 = 0;
						for (int i = 0; i < acc.Control2s.Count; i++) {
							Control2 c2 = acc.Control2s[i];
							if (c2.isLocked)
								isLocked[i] = true;

							if (c2.cb.Checked && c2.fillWt > 0 && !isLocked[i]) {
								int minDH = 0;
								if (first) {
									// reset dh to zero the first time because the
									// negative dh is aggregated.
									c2.dh = 0;
									minDH = c2.MinDH;
									minDHs[i] = minDH; // cache MinDH
								}
								else {
									minDH = minDHs[i];
								}

								double ddh = c2.fillWt * eh / totalWt;
								int dh = (int) ddh;

								pixels2 += ddh % 1; // pixel perfect
								if (pixels2 <= -0.5) {
									dh--;
									pixels2++;
								}

								int dhOrig = c2.dh;
								c2.dh = c2.dh + dh;
								if (c2.dh <= minDH) {
									c2.dh = minDH;
									isLocked[i] = true;
								}
								int shedded = c2.dh - dhOrig;
								mh2 += shedded;
							}
						}
						eh = eh - mh2;
						first = false;
					} while (mh2 < 0 && eh < 0);
				}
				else if (eh > 0 && totalWt > 0) {
					// max-height constraints are handled by using the isLocked[]
					// to treat the Control2 as locked.
					// when a control maxes out its size, then its fillWt is no longer used
					// and the excess space can be used by other controls. However, the increase in
					// space and decrease in totalWt means that other controls might now exceed their
					// max height too! So loop until none of the controls exceed their max height.
					// Perhaps there is a more efficient approach.
					bool[] isLocked = new bool[acc.Control2s.Count];
					int[] maxDHs = new int[acc.Control2s.Count];
					int mh2 = 0;
					bool first = true;
					do {
						mh2 = 0;
						double pixels2 = 0;
						double totalWt2 = 0;
						for (int i = 0; i < acc.Control2s.Count; i++) {
							Control2 c2 = acc.Control2s[i];
							if (c2.isLocked)
								isLocked[i] = true;

							if (c2.cb.Checked && c2.fillWt > 0 && !isLocked[i]) {
								double ddh = c2.fillWt * eh / totalWt;
								int dh = (int) ddh;

								pixels2 += ddh % 1;
								if (pixels2 >= 0.5) {
									dh++;
									pixels2--;
								}

								int maxDH = 0;
								if (first) {
									// cache the maxDH is more efficient
									maxDH = c2.MaxDH;
									maxDHs[i] = maxDH;

								}
								else {
									maxDH = maxDHs[i];
								}

								if (dh >= maxDH) {
									isLocked[i] = true;
									c2.dh = maxDH;
									mh2 += maxDH;
								}
								else {
									totalWt2 += c2.fillWt;
								}
							}
						}
						totalWt = totalWt2;
						eh = eh - mh2;
						first = false;
					} while (mh2 > 0 && eh > 0);

					if (totalWt > 0) {
						// if totalWt is zero, that means no controls with a fillWt are currently open
						// or the ones with fillWt > 0 have maxed out their size

						double pixels = 0; // pixel perfect
						for (int i = 0; i < acc.Control2s.Count; i++) {
							if (isLocked[i]) // height is locked or pseudo-locked, do nothing
								continue;

							Control2 c2 = acc.Control2s[i];
							if (!c2.cb.Checked || c2.fillWt <= 0)
								continue;

							double ddh = c2.fillWt * eh / totalWt;
							int dh = (int) ddh;

							pixels += ddh % 1;
							if (pixels >= 0.5) {
								dh++;
								pixels--;
							}

							if (fillModeGrowOnly) {
								if (dh > c2.dh)
									c2.dh = dh;
								else {} // do nothing
							}
							else
								c2.dh = dh;
						}
					}
				}
			}
		}
	}

	private class ToolBox : ToolStripDropDown {
		ToolStripSplitButton miPack = new ToolStripSplitButton("\u2191") { ToolTipText = "Pack", Anchor = AnchorStyles.Left | AnchorStyles.Right }; // up arrow
		ToolStripButton miPackAll = new ToolStripButton("\u21c8") { ToolTipText = "Pack All" }; // two up arrows side by side
		ToolStripButton miCloseAll = new ToolStripButton("\u23EB") { ToolTipText = "Close All" }; // two up triangles stacked vertically

		ToolStripSplitButton miFill = new ToolStripSplitButton("\u2193") { ToolTipText = "Fill", Anchor = AnchorStyles.Left | AnchorStyles.Right }; // down arrow
		ToolStripButton miFillAll = new ToolStripButton("\u21ca") { ToolTipText = "Fill All" }; // two down arrows side by side
		ToolStripButton miOpenAll = new ToolStripButton("\u23EC") { ToolTipText = "Open All" }; // two down triangles stacked vertically

		ToolStripSplitButton miLock = new ToolStripSplitButton("\uD83D\uDD12") { ToolTipText = "", Anchor = AnchorStyles.Left | AnchorStyles.Right }; // lock-open / lock-close (toggle)
		ToolStripButton miLockAll = new ToolStripButton("\uD83D\uDD10") { ToolTipText = "Lock All" }; // lock with key
		ToolStripButton miUnlockAll = new ToolStripButton("\uD83D\uDD11") { ToolTipText = "Unlock All" }; // key

		Control2 _c2 = null;

		public ToolBox() {

			var menu = this;
			menu.Padding = Padding = new Padding(3, 2, 3, 1);
			//menu.LayoutStyle = ToolStripLayoutStyle.HorizontalStackWithOverflow;
			menu.DropShadowEnabled = false;
			menu.Items.Add(miPack);
			menu.Items.Add(miFill);
			menu.Items.Add(miLock);
			menu.BackColor = Color.Transparent;
			//menu.DefaultDropDownDirection = ToolStripDropDownDirection.BelowRight;

			miPack.DropDown = new ToolStripDropDown();
			miPack.DropDown.Padding = new Padding(3, 2, 1, 1);
			//miPack.Margin = new System.Windows.Forms.Padding(10);
			//miPack.DropDown.LayoutStyle = ToolStripLayoutStyle.VerticalStackWithOverflow;
			miPack.DropDown.LayoutStyle = ToolStripLayoutStyle.HorizontalStackWithOverflow;
			miPack.DropDown.DropShadowEnabled = false;
			miPack.DropDown.Items.Add(miPackAll);
			miPack.DropDown.Items.Add(miCloseAll);

			miFill.DropDown = new ToolStripDropDown();
			miFill.DropDown.Padding = new Padding(3, 2, 1, 1);
			miFill.DropDown.LayoutStyle = ToolStripLayoutStyle.HorizontalStackWithOverflow;
			miFill.DropDown.DropShadowEnabled = false;
			miFill.DropDown.Items.Add(miFillAll);
			miFill.DropDown.Items.Add(miOpenAll);

			miLock.DropDown = new ToolStripDropDown();
			miLock.DropDown.Padding = new Padding(3, 2, 1, 1);
			miLock.DropDown.LayoutStyle = ToolStripLayoutStyle.HorizontalStackWithOverflow;
			miLock.DropDown.DropShadowEnabled = false;
			miLock.DropDown.Items.Add(miLockAll);
			miLock.DropDown.Items.Add(miUnlockAll);

			Action<Object> fillAction = (src) => {
				Current.cb.Focus();
				Accordion a = (Accordion) Current.Parent;
				Size ps = a.layoutEngine.GetPreferredSize(a, true, true, false);
				Size cs = a.ClientSize;
				int eh = cs.Height - ps.Height;
				Current.lastClicked = DateTime.Now;

				if (src == miFill) {
					if (eh > 0) {
						int oh = 0;
						if (!Current.cb.Checked) {
							Current.dh = 0;
							Size ps2 = Current.GetPackSize();
							oh = ps2.Height;
							if (ps.Width > cs.Width)
								oh += SystemInformation.HorizontalScrollBarHeight;
						}
						bool isLocked = Current.isLocked;
						Current.isLocked = true;
						Current.dh += Math.Min(Current.MaxDH, Math.Max(eh - oh, 0));
						// since extra space exists, only one perform layout is required
						// because scrollbars won't change
						//a.InternalPerformLayout();
						a.PerformLayout();
						Current.isLocked = isLocked;
					}
					else {
						// filling a control when all the extra height is already taken up
						// will expand the checkbox and control to the full client height
						if (!Current.cb.Checked) {
							Current.dh = 0;
						}

						// it looks odd to expand into the padding area (which will require scrollbars)
						// when there is only a single checkbox and control visible
						int numCheckBoxVisible = 0;
						int numControl2Visible = 0;
						foreach (Control2 c2 in a.Control2s) {
							if (c2.Visible) {
								numControl2Visible++;
								if (numControl2Visible > 1)
									break;
							}
							if (c2.cb.Visible) {
								numCheckBoxVisible++;
								if (numCheckBoxVisible > 1)
									break;
							}
						}
						int padding = 0;
						if (numCheckBoxVisible == 1 && numControl2Visible == 1)
							padding = a.Padding.Vertical;

						Size s = Current.GetPackSize();
						// only add the top margin of Control2 and bottom margin of the checkbox
						//s.Height += Current.Margin.Top + Current.cb.Margin.Bottom - 2;
						int availH = cs.Height - (padding + Current.Margin.Top + Current.cb.Margin.Bottom + Current.cb.Height + s.Height);
						if (Current.ResizeBar != null)
							availH -= (Current.ResizeBar.Height / 2);

						int dhNew = Math.Min(Current.MaxDH, Math.Max(Current.dh, availH));
						if (Current.dh == dhNew)
							return;

						Current.dh = dhNew;
						bool lockOrig = Current.isLocked;
						Current.isLocked = true;
						a.InternalPerformLayout();

						a.isOpening = true;
						a.scrollToBottom = true;
						a.ScrollControlIntoView(Current);
						a.scrollToBottom = false;
						a.ScrollControlIntoView(Current.cb);
						a.isOpening = false;
						Current.isLocked = lockOrig;
					}
				}
				else if (src == miFillAll) {
					// preference is given to controls that have fillWt > 0
					// extra space is allocated equally, regardless of fillWt
					if (eh > 0) {
						int numOpen = 0;
						int numOpenWithPositiveFillWt = 0;
						foreach (Control2 c2 in a.Control2s) {
							if (c2.cb.Checked) {
								numOpen++;
								if (c2.fillWt > 0)
									numOpenWithPositiveFillWt++;
							}
						}
						if (numOpen == 0)
							return; // no controls are open
						if (a.GrabRequiresPositiveFillWeight && numOpenWithPositiveFillWt == 0)
							return; // no controls are open with positive fillWt

						int x = (numOpenWithPositiveFillWt > 0 ? numOpenWithPositiveFillWt : numOpen);

						double pixel = 0;
						foreach (Control2 c2 in a.Control2s) {
							c2.Tag = c2.isLocked;
							c2.isLocked = true;
							if (c2.cb.Checked) {
								if (numOpenWithPositiveFillWt > 0 && c2.fillWt <= 0)
									continue;

								double hh = 1.0 * eh / x;
								int ihh = (int) hh;
								pixel += hh % 1;
								if (pixel >= 0.5) {
									ihh++;
									pixel--;
								}
								int newDH = c2.dh + ihh;
								int maxDH = c2.MaxDH;
								if (newDH >= maxDH) {
									newDH = maxDH;
									int alloc = maxDH - c2.dh;
									eh = Math.Max(0, eh - alloc);
									x--;
								}
								c2.dh = newDH;
							}
						}
						a.PerformLayout();
						foreach (Control2 c2 in a.Control2s)
							c2.isLocked = (bool) c2.Tag;
					}
				}
				else if (src == miOpenAll) {
					Current.lastClicked = DateTime.Now;
					a.Open(null);
				}
			};

			miFill.ButtonClick += delegate {
				fillAction(miFill);
			};

			miFill.DropDown.ItemClicked += (o, e) => {
				fillAction(e.ClickedItem);
			};

			Action<Object> packAction = (src) => {
				//Current.cb.Focus(); // why?
				var host = (Accordion) Current.Parent;
				if (src == miPack || src == miPackAll) {
					foreach (Control2 c2 in host.Control2s) {
						c2.Tag = c2.isLocked;
						c2.isLocked = true;
						if (c2 == Current || src == miPackAll) {
							c2.dh = 0;
							//c2.lastClicked = DateTime.MinValue;
						}
					}

					//host.UpdateDeltaHeights();
					host.InternalPerformLayout();

					foreach (Control2 c2 in host.Control2s)
						c2.isLocked = (bool) c2.Tag;

					Current.lastClicked = DateTime.Now;
				}
				else if (src == miCloseAll) {
					host.Close(null);
				}
			};

			miPack.ButtonClick += delegate {
				packAction(miPack);
			};

			miPack.DropDownItemClicked += (o,e) => {
				packAction(e.ClickedItem);
			};

			Action<Object> lockAction = (src) => {
				Current.cb.Focus();
				Current.lastClicked = DateTime.Now;
				Accordion host = (Accordion) Current.Parent;
				if (src == miLockAll || src == miUnlockAll) {
					foreach (Control2 c2 in host.Control2s)
						c2.isLocked = (src == miLockAll);
				}
				else {
					Current.isLocked = !Current.isLocked;
					//if (!Current.isLocked)
				}

				//host.UpdateDeltaHeights();
				host.InternalPerformLayout();
			};

			miLock.ButtonClick += delegate {
				lockAction(miLock);
			};
			miLock.DropDown.ItemClicked += (o,e) => {
				lockAction(e.ClickedItem);
			};
		}

		DateTime leaveTime;
		protected override void OnMouseLeave(EventArgs e) {
 			base.OnMouseLeave(e);
			ToolBox toolBox = this;

			// the tooltip of a menu item causes a mouse leave, so
			// confirm the mouse is outside of the bounds before hiding
			leaveTime = DateTime.Now;
			new System.Threading.Thread((o) => {
				// allow the mouse to leave for up to 1 second before closing
				System.Threading.Thread.Sleep(1000);
				if ((DateTime) o != leaveTime)
					return;

				// it's possible that the thread sleeps and when it wakes up
				// the form was closed and the toolBox is disposed.
				if (!toolBox.IsDisposed) {
					toolBox.BeginInvoke((Action) delegate {
						if (!IsMouseHit(Control.MousePosition)) {
							toolBox.Hide();
						}
					});
				}
			}).Start(leaveTime);
		}

		private bool IsMouseHit(Point pt) {
			if (this.Bounds.Contains(pt))
				return true;

			if (miPack.DropDown.Visible && miPack.DropDown.Bounds.Contains(pt))
				return true;

			if (miFill.DropDown.Visible && miFill.DropDown.Bounds.Contains(pt))
				return true;

			if (miLock.DropDown.Visible && miLock.DropDown.Bounds.Contains(pt))
				return true;

			return false;
		}


		public Control2 Current {
			get {
				return _c2;
			}
			set {
				_c2 = value;
				if (_c2 == null)
					return;

				Accordion a = (Accordion) _c2.Parent;
				Size ps = a.layoutEngine.GetPreferredSize(a, true, true, false);
				Size cs = a.ClientSize;
				int eh = cs.Height - ps.Height;

				bool hasLocked = false;
				bool hasUnlocked = false;
				bool hasOpen = false;
				bool hasOpenPositiveFillWt = false;
				bool hasOpenPositiveExtraHeight = false;
				int numClosed = 0;
				foreach (Control2 c2 in a.Control2s) {
					if (!c2.cb.Visible)
						continue;

					if (c2.isLocked)
						hasLocked = true;
					else
						hasUnlocked = true;

					if (c2.cb.Checked) {
						hasOpen = true;
						if (c2.fillWt > 0)
							hasOpenPositiveFillWt = true;
						if (c2.dh > 0)
							hasOpenPositiveExtraHeight = true;
					}
					else
						numClosed++;
				}

				miUnlockAll.Enabled = hasLocked;
				miLockAll.Enabled = hasUnlocked;
				miFillAll.Enabled = (hasOpenPositiveFillWt || hasOpen && !a.GrabRequiresPositiveFillWeight) && eh > 0;
				miOpenAll.Enabled = numClosed > 0 && !a.OpenOneOnly; // || !hasOpen && numClosed == 1;
				miCloseAll.Enabled = hasOpen;
				miPack.Enabled = hasOpen;
				miPackAll.Enabled = hasOpenPositiveExtraHeight;

				if (_c2.isLocked) {
					miLock.ToolTipText = "Unlock height.";
					miLock.Text = "\uD83D\uDD13";
				}
				else {
					miLock.ToolTipText = "Lock height.";
					miLock.Text = "\uD83D\uDD12";
				}
			}
		}

		protected override void OnFontChanged(EventArgs e) {
			base.OnFontChanged(e);
			// the sub dropdown menus don't inherit
			foreach (ToolStripDropDownItem item in Items) {
				if (item.DropDown != null)
					item.DropDown.Font = Font;
			}
		}
	}

	protected override void Dispose(bool disposing) {
		base.Dispose(disposing);
		if (disposing) {
			if (tips != null)
				tips.Dispose();

			if (toolBox != null)
				toolBox.Dispose();

			Application.RemoveMessageFilter(this);

			tips = null;
			toolBox = null;
		}
	}


	[DllImport("user32.dll")]
	private static extern bool AnimateWindow(IntPtr hwnd, int dwTime, int dwFlags);

	[DllImport("user32.dll")]
	public static extern int SendMessage(IntPtr hWnd, Int32 wMsg, bool wParam, Int32 lParam);

	[DllImport("user32.dll")]
	public static extern bool ReleaseCapture();

	[DllImport("user32.dll")]
	extern static IntPtr GetForegroundWindow();

	[DllImport("user32.dll")]
	public static extern IntPtr GetParent(IntPtr hWnd);

	[DllImport("user32.dll")]
	private static extern IntPtr WindowFromPoint(Point pt);

	[DllImport("user32.dll")]
	private static extern IntPtr GetFocus(); // returns the window handle with the active focus

	[DllImport("user32.dll")]
	private static extern IntPtr SetFocus(IntPtr hWnd);

	[DllImport("user32.dll")]
	private static extern bool GetWindowRect(IntPtr hWnd, out RECT lpRect);

	[DllImport("user32.dll")]
	private static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

	[StructLayout(LayoutKind.Sequential)]
	private struct RECT {
		public int Left;
		public int Top;
		public int Right;
		public int Bottom;
	}

	private static bool AnimateWindow(Control c, int dwTime, AnimateWindowFlags dwFlags) {
		int flags = (int) dwFlags;
		if (flags == 0)
			return false;

		return AnimateWindow(c.Handle, dwTime, flags);
	}

	// get the control directly under the point
	// traverse up and check if any parent control is this control
	private bool IsMouseOverThisControl(Point pt) {
		// this approach may be better suited if hosting WPF controls:
		IntPtr hWnd = WindowFromPoint(pt);
		IntPtr h = this.Handle;
		while (hWnd != IntPtr.Zero) {
			if (hWnd == h)
				return true;

			hWnd = GetParent(hWnd);
		}

		return false;
		//Control c = ControlAtPoint(pt);
		//while (c != null) {
		//	if (c == this)
		//		return true;
		//	c = c.Parent;
		//}
		//return false;
	}

	private static IntPtr GetTopMostHandle(IntPtr hWnd) {
		while (true) {
			IntPtr parent = GetParent(hWnd);
			if (parent == IntPtr.Zero)
				break;
			hWnd = parent;
		}
		return hWnd;
	}

	private static Control ControlAtPoint(Point pt) {
		IntPtr hWnd = WindowFromPoint(pt);
		if (hWnd != IntPtr.Zero)
			return Control.FromHandle(hWnd);
		return null;
	}

	//-----

	public interface ICheckBoxFactory {
		CheckBox CreateCheckBox(String text, bool check, Padding margin);
	}

	///<summary>The default checkbox factory uses the 'Appearance.Button' and anchors
	///the checkbox such that it will span the width of the accordion.</summary>
	public class DefaultCheckBoxFactory : ICheckBoxFactory {
		public virtual CheckBox CreateCheckBox(String text, bool check, Padding margin) {
			CheckBox cb = new CheckBox();
			cb.Appearance = Appearance.Button;
			//cb.AutoSize = true; // AutoSize must be true or the text will wrap under and be hidden
			cb.Checked = check;
			cb.Text = text;
			cb.Anchor = AnchorStyles.Left | AnchorStyles.Right; // cb.Dock = DockStyle.Fill also works.
			cb.Margin = margin; // typically 0 so that no are gaps between the buttons
			cb.AutoEllipsis = true;
			return cb;
		}
	}

	public interface IResizeBarFactory {
		Control CreateResizeBar(Padding margin);
	}

	///<summary>The default resize bar factory uses the Opulos.Core.UI.ResizeBar
	///class which has a modern look.</summary>
	public class DefaultResizeBarFactory : IResizeBarFactory {
		public virtual Control CreateResizeBar(Padding margin) {
			ResizeBar bar = new ResizeBar();
			bar.Margin = new Padding(margin.Left, 0, margin.Right, 0);
			return bar;
		}
	}
}

[Flags]
public enum AnimateWindowFlags : int {

	///<summary>Disable animation effects.</summary>
	None = 0,

	///<summary>Shows the window. Do not use this value with Hide.</summary>
	Show = 0x00020000,

	///<summary>Hides the window. By default, the window is shown.</summary>
	Hide = 0x00010000,

	// As per the documentation, only works on top-level windows, so not applicable for Accordion.
	/////<summary>Uses a fade effect. This flag can be used only if hwnd is a top-level window.</summary>
	//Blend = 0x00080000,

	///<summary>Makes the window appear to collapse inward if Hide is used or expand outward if the Show is used. The various direction flags have no effect.</summary>
	Center = 0x00000010,

	///<summary>Uses slide animation. By default, roll animation is used. This flag is ignored when used with Center.</summary>
	Slide = 0x00040000,

	///<summary>Animates the window from left to right. This flag is used with the Slide flag. It is ignored when used with Center.</summary>
	HorizontalPositive = 0x00000001,

	///<summary>Animates the window from right to left. This flag is used with the Slide flag. It is ignored when used with Center.</summary>
	HorizontalNegative = 0x00000002,

	///<summary>Animates the window from top to bottom. This flag is used with the Slide flag. It is ignored when used with Center.</summary>
	VerticalPositive = 0x00000004,

	///<summary>Animates the window from bottom to top. This flag is used with the Slide. It is ignored when used with Center.</summary>
	VerticalNegative = 0x00000008,
}

}
