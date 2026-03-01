import asyncio

import reflex as rx


class SamplesState(rx.State):
    """UI state local to the samples page."""

    code_copied_id: str = ""

    async def copy_code(self, code: str, code_id: str):
        """Copy a samples code block and flash copy feedback on that block."""
        self.code_copied_id = ""
        yield
        self.code_copied_id = code_id
        yield rx.set_clipboard(code)
        await asyncio.sleep(1.2)
        if self.code_copied_id == code_id:
            self.code_copied_id = ""


__all__ = ["SamplesState"]
