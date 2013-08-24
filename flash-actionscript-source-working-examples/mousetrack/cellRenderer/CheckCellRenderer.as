import mx.core.UIComponent
import mx.controls.CheckBox
class CheckCellRenderer extends mx.controls.cells.CheckCellRenderer
{
	function click()
	{
		super.click()
		listOwner.selectedIndex = getCellIndex().itemIndex
		listOwner.dispatchEvent({ type:"cellPress"});
	}
}
