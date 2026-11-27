import asyncio
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, HookMatcher


async def bloquear_comandos_peligrosos(input_data, tool_use_id, context):
    if input_data.get("tool_name") == "Bash":
        comando = input_data.get("tool_input", {}).get("command", "")
        if "rm -rf" in comando:
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Comando destructivo bloqueado por hook.",
                }
            }
    return {}


async def registrar_despues_de_herramienta(input_data, tool_use_id, context):
    herramienta = input_data.get("tool_name")
    print(f"[PostToolUse] Se ejecutó la herramienta: {herramienta}")
    return {}


async def main():
    opciones = ClaudeAgentOptions(
        hooks={
            "PreToolUse": [
                HookMatcher(
                    matcher="Bash",
                    hooks=[bloquear_comandos_peligrosos],
                )
            ],
            "PostToolUse": [
                HookMatcher(
                    matcher=".*",
                    hooks=[registrar_despues_de_herramienta],
                )
            ],
        }
    )

    async with ClaudeSDKClient(options=opciones) as client:
        await client.query("Lista los archivos del directorio actual.")
        async for mensaje in client.receive_response():
            print(mensaje)


if __name__ == "__main__":
    asyncio.run(main())
